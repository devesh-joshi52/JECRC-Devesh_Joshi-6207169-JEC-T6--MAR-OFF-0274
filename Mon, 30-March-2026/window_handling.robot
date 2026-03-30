*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/windows

*** Test Cases ***
Handling Windows
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    3s

    Click Element    xpath=//a[@href="/windows/new"]
    Sleep    3s

    @{windows}  Get Window Handles
    @{titles}  Get Window Titles
    Log To Console    ${titles}

    Switch Window  NEW
    
    Page Should Contain    New Window
    Page Should Contain Element   xpath=//h3[text()="New Window"]

    Switch Window  ${windows}[0]
    Sleep    3s

    Close Browser