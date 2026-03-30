*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Task_1
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    3s

    Scroll Element Into View    id=PopUp
    Sleep    3s

    Click Element    id=PopUp
    Sleep    3s
    
    @{windows}  Get Window Handles
    @{titles}  Get Window Titles
    Log To Console    ${titles}[1]
    Switch Window  ${windows}[1]
    Maximize Browser Window
    Sleep    4s

    Switch Window  ${windows}[2]
    Maximize Browser Window
    Log To Console    ${titles}[2]
    Sleep    3s

    Switch Window  ${windows}[0]
    Maximize Browser Window
    Log To Console    ${titles}[0]
    Page Should Contain Element    xpath=//h1[@class="title"]
    sleep   2s

    Close Browser