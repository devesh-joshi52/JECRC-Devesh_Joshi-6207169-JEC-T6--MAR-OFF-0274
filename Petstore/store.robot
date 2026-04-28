#pip install robotframework-requests
#pip install robotframework-jsonlibrary
#pip install jsonschema

*** Settings ***
Library    RequestsLibrary
Library    Collections
Library    String

*** Variables ***
${BASE_URL}    https://petstore.swagger.io/v2

*** Test Cases ***

Pet inventories
    [Documentation]  Get pet inventories by status
    Create Session    petapi    ${BASE_URL}    verify=True

    ${response}=    GET On Session    petapi    /store/inventory

    Should Be Equal As Integers    ${response.status_code}    200

    ${body}=    Set Variable    ${response.json()}

    Log To Console    ${body}
    Log To Console    ${response.status_code}


Place Order
    [Documentation]  Place an order for a pet
    Create Session   petapi     ${BASE_URL}     verify=True

    ${payload}=     Create Dictionary
    ...     id=12345
    ...     petId=54321
    ...     quantuty=1
    ...     shipDate=2026-04-28T06:56:01.3962
    ...     status=placed
    ...     complete=true

    ${response}=    POST On Session     petapi      /store/order        json=${payload}

    Should Be Equal As Integers    ${response.status_code}    200
    ${body}=  Set Variable      ${response.json()}

    Should Be Equal As Integers    ${body}[id]    12345
    Should Be Equal As Strings    ${body}[status]    placed

    Log To Console    ${body}
    Log To Console    ${response.status_code}

    Set Suite Variable    ${ORDER_ID}    ${body}[id]


Get Order By ID
    [Documentation]  Place an order and retrieve it by ID
    Create Session   petapi     ${BASE_URL}     verify=True
    ${response}=    GET On Session     petapi      /store/order/${ORDER_ID}


    Log To Console    ${response.status_code}
    Log To Console    ${response.json()}

Delete Order By ID
    [Documentation]  Place an order and delete it by ID
    Create Session   petapi     ${BASE_URL}     verify=True
    ${response}=    DELETE On Session     petapi      /store/order/${ORDER_ID}

    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.status_code}
    Log To Console    ${response.json()}


E2E
    [Documentation]  Place an order, retrieve it, and delete it
    Create Session   e2eapi     ${BASE_URL}     verify=True

    # Place an order
    ${payload}=     Create Dictionary
    ...     id=12345
    ...     petId=54321
    ...     quantuty=1
    ...     shipDate=2026-04-28T06:56:01.3962
    ...     status=placed
    ...     complete=true

    ${res1}=    POST On Session     e2eapi      /store/order        json=${payload}
    Should Be Equal As Integers    ${res1.status_code}    200
    Log To Console    Created an order

    ${body}=  Set Variable      ${res1.json()}
    Set Suite Variable    ${ORDER_ID}    ${body}[id]

    # Retrieve the order by ID
    ${res2}=    GET On Session     e2eapi      /store/order/${ORDER_ID}
    Should Be Equal As Integers    ${res2.status_code}    200
    Log To Console    Get the order by id

    # Delete the order by ID
    ${res3}=    DELETE On Session     e2eapi      /store/order/${ORDER_ID}
    Should Be Equal As Integers    ${res3.status_code}    200
    Log To Console    e2e successfully completed

