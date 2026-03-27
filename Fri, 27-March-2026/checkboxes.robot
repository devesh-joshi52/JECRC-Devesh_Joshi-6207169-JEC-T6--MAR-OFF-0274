*** Settings ***
Documentation  handling checkboxes
Library  SeleniumLibrary

*** Variables ***
${url}  http://the-internet.herokuapp.com/
${2url}  https://testautomationpractice.blogspot.com/


*** Test Cases ***
Handling Checkboxes
    [Documentation]  herokuapp checkbox
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Click Element    xpath=//a[text()="Checkboxes"]

    Page Should Contain Checkbox    xpath=(//input[@type="checkbox"])[1]

    Select Checkbox    xpath=(//input[@type="checkbox"])[1]

    Sleep    2s
    Unselect Checkbox    xpath=(//input[@type="checkbox"])[2]
    Sleep    2s



More Checkboxes
    [Documentation]  herokuapp checkbox
    Open Browser  ${2url}  chrome
    Maximize Browser Window
    Sleep    2s
    
    
    Page Should Contain Radio Button    xpath=//input[@id='male']
    Click Element    xpath=//input[@id='male']

    Select Checkbox    xpath=//input[@id='sunday']
    Sleep    2s
    
    Select Checkbox    xpath=//input[@id='monday']
    Sleep    2s
    
    Select Checkbox    xpath=//input[@id='tuesday']
    Sleep    2s
    
    Select Checkbox    xpath=//input[@id='wednesday']
    Sleep    2s
    
    Select Checkbox    xpath=//input[@id='thursday']
    Sleep    2s
    
    Select Checkbox    xpath=//input[@id='friday']
    Sleep    2s

    Select Checkbox    xpath=//input[@id='saturday']
    Sleep    2s    
    
    Close Browser