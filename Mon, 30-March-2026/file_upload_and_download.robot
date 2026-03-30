*** Settings ***
Library  SeleniumLibrary
Library    XML
Library    OperatingSystem

*** Variables ***
${url}  https://the-internet.herokuapp.com/
${chech_downloads}  C:\\Users\\jdeve\\Downloads\\file.txt

*** Test Cases ***
Upload
    Open Browser  ${url}  chrome
    Maximize Browser Window
    
    Click Element    xpath=//a[@href="/upload"]
    Sleep    2s

    ${path}  Normalize Path  ${CURDIR}/sample.txt

    Choose File    id=file-upload    ${path}
    Sleep    3s

    Click Button    id=file-submit

    Close Browser


Download
    Open Browser  ${url}  chrome
    Maximize Browser Window

    Click Element    xpath=//a[@href="/download"]
    Sleep    2s

    Click Element    xpath=//a[@href="download/file.txt"]
    Sleep    2s

    Wait Until Created    ${chech_downloads}  timeout=10s

    File Should Exist    ${chech_downloads}
    Log To Console    It downloaded succesfully !!

    Close Browser