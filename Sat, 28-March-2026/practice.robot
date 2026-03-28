*** Settings ***
Documentation  handling multi select
Library  SeleniumLibrary

*** Variables ***
${url}  https://in.bookmyshow.com/explore/home/jaipur

*** Test Cases ***
multi select
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s

