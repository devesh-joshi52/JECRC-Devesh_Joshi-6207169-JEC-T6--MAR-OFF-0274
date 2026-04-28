*** Settings ***
Library    RequestsLibrary
Library    Collections
Library    JSONLibrary

*** Variables ***
${BASE_URL}    https://petstore.swagger.io/v2

*** Test Cases ***
# Create a new pet
Add Pet
    [Documentation]  Add a new pet to the store
    Create Session   petapi     ${BASE_URL}     verify=True

    ${payload}=    Load Json From File    ${CURDIR}/../data/add_pet.json

    ${response}=    POST On Session     petapi     /pet    json=${payload}

    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.json()}

    ${body}=    Set Variable    ${response.json()}
    Should Be Equal As Integers    ${body}[id]    55
    Should Be Equal As Strings     ${body}[name]  ubantu
    Set Suite Variable    ${PET_ID}    ${body}[id]

# Update an existing pet
Update Pet
    [Documentation]  Update an existing pet in the store
    Create Session   petapi     ${BASE_URL}     verify=True

    ${payload}=    Load Json From File    ${CURDIR}/../data/updated_pet.json

    ${response}=    PUT On Session     petapi      /pet        json=${payload}

    Should Be Equal As Integers    ${response.status_code}    200

    ${body}=    Set Variable    ${response.json()}
    Should Be Equal As Integers    ${body}[id]    55
    Should Be Equal As Strings     ${body}[name]  Updated
    Should Be Equal As Strings     ${body}[status]  sold
    Log To Console    ${body}

Get Pet By ID
    [Documentation]  Retrieve a pet by its ID
    Create Session   petapi     ${BASE_URL}     verify=True

    ${payload}=    Load Json From File    ${CURDIR}/../data/updated_pet.json

    ${response}=    GET On Session     petapi      /pet/${PET_ID}

    Should Be Equal As Integers    ${response.status_code}    200

    ${body}=    Set Variable    ${response.json()}
    Should Be Equal As Integers    ${body}[id]    55
    Should Be Equal As Strings     ${body}[name]  Updated
    Should Be Equal As Strings     ${body}[status]  sold
    Log To Console    ${body}


Upload an Image
    [Documentation]  Upload an image for a pet
    Create Session   petapi     ${BASE_URL}     verify=True

    ${form_data}=    Create Dictionary  additionalMetadata=Sample image for pet
    ${file_path}=   Set Variable    ${CURDIR}/../data/ubantu_image.jpg

    ${file}=  Evaluate    {'file': open($file_path, 'rb')}

    ${response}=    POST On Session     petapi      /pet/55/uploadImage
    ...  data=${form_data}
    ...  files=${file}

    Should Be Equal As Integers    ${response.status_code}    200


Update Pet With Form Data
    [Documentation]  Updates a pet in the store with form data
    Create Session   petapi     ${BASE_URL}     verify=True

    &{form_data}=    Create Dictionary    name=FormUpdatedPet    status=pending

    ${response}=    POST On Session     petapi      /pet/${PET_ID}    data=${form_data}

    Should Be Equal As Integers    ${response.status_code}    200

    ${body}=    Set Variable    ${response.json()}
    Log To Console    ${body}


Delete Pet
    [Documentation]  Deletes a pet by ID
    Create Session   petapi     ${BASE_URL}     verify=True

    ${response}=    DELETE On Session     petapi      /pet/${PET_ID}

    Should Be Equal As Integers    ${response.status_code}    200

    ${body}=    Set Variable    ${response.json()}
    Log To Console    ${body}
