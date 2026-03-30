*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://demo.automationtesting.in/Frames.html

*** Test Cases ***
Iframes
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Select Frame    id=singleframe

    Input Text    xpath=//input[@type="text"]    Dev
    Sleep    3s
    Unselect Frame

    Close Browser