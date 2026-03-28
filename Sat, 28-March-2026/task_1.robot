*** Settings ***
Documentation  handling multi select
Library  SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
multi select
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Click Element    xpath=(//div[@class='form-group'])[6]

    Page Should Contain List    xpath=(//select[@class='form-control'])[2]

    ${color}=  Get List Items    id=colors
    Log To Console    ${color}

    Select From List By Label   id=colors   Blue
    Select From List By Label   id=colors   Yellow


    @{select_color}=  Get Selected List Labels    id=colors
    Log To Console    ${select_color}
    Sleep    3s

    Close Browser