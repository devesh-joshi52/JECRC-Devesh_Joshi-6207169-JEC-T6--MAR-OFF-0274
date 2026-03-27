*** Settings ***
Documentation  Opening browser
Library  SeleniumLibrary


*** Variable ***
#scarlar variables
${url}  https://www.cricbuzz.com/

#list variables
@{bikes}  ktm  kwasaki  honda  pulsar

#dict variables
&{cars}  nissan=gtr  honda=civic  bmw=m4

*** Test Cases ***
Opening Chrome headless Browser
    [Documentation]  Chrome browser navigating to https://www.cricbuzz.com/
    [Tags]  smoke
    Open Browser  ${url}  headlesschrome
    Maximize Browser Window

    Log    navigated to cricbuzz
    Log To Console    ${bikes}[1]
    Log To Console    ${cars.nissan}
    Sleep    5s

    Close Browser

Open cricbuz in edge
    Open Edge Browser


*** Keywords ***
Open Edge Browser
    [Documentation]  Edge browser navigating to https://www.cricbuzz.com/
    [Tags]  smoke
    Open Browser  ${url}  edge
    Maximize Browser Window

    Log    navigated to cricbuzz
    Log To Console    ${bikes}[1]
    Log To Console    ${cars.nissan}
    Sleep    5s

    Close Browser