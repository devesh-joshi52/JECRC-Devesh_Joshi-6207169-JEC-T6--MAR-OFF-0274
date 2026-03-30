*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/

*** Test Cases ***
Implicit wait
    Open Browser  ${url}  chrome
    ${before}  Get Selenium Implicit Wait
    Log To Console    ${before}

    Set Selenium Implicit Wait    5s
    ${after}  Get Selenium Implicit Wait
    Log To Console    ${after}

    Close Browser


