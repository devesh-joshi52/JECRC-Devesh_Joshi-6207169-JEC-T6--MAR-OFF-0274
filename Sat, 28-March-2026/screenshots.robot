*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://in.bookmyshow.com/explore/home/jaipur

*** Test Cases ***
Screenshots
    Set Screenshot Directory    ${CURDIR}/Screenshots

    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Capture Page Screenshot  fullpage.png

    Scroll Element Into View    xpath=//div[text()="Project Hail Mary"]
    Sleep    2s
    Capture Element Screenshot    xpath=//img[@alt="Project Hail Mary"]   Ryan_Gosling.png
    Sleep    2s

    Close Browser