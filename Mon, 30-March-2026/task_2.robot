*** Settings ***
Library  SeleniumLibrary
Library    XML

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Simple Alert
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    3s

    Click Button    id=alertBtn
    Sleep    2s
    Handle Alert
    Sleep    2s

    Close Browser

Confirmation Alert
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    3s

    Click Button    id=confirmBtn
    Sleep    2s
    Handle Alert  action=DISMISS
    Sleep    2s

    ${content}  Get Text    xpath=//p[@id="demo"]

    Page Should Contain    You pressed Cancel!
    Log To Console    ${content}
    Sleep    2s

    Close Browser


Prompt Alert
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    3s

    Click Button    id=promptBtn
    Sleep    2s

    Input Text Into Alert    Devesh
    Sleep    2s

    Page Should Contain    Hello Devesh! How are you today?
    Sleep    2s

    ${content}  Get Text    xpath=//p[@id="demo"]

    Log To Console    ${content}

    Close Browser

