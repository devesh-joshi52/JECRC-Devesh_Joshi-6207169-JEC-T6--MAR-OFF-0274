*** Settings ***
Documentation  Opening browser
Library  SeleniumLibrary
*** Variable ***
*** Test Cases ***
Opening Edge headless Browser
    [Documentation]  Edge browser navigating to https://www.cricbuzz.com/
    Open Browser  https://www.cricbuzz.com/  headlessedge
    Maximize Browser Window

    Log    navigated to cricbuzz
    Log To Console    navigated to cricbuzz
    Sleep    5s

    Close Browser