#Navigate to amazon
#Click on electronic in tab
#Check on 'boat' checkbox
#click on any product before clicking store the name of product
#switch to new window
#assert the product name is present in the new window
#print the actual price, discounted price and the percentage
#scroll to add to cart and click on the button
#click on cart icon on top right corner
#check if same product has been added

*** Settings ***
Library  SeleniumLibrary
Library    XML

*** Variables ***
${url}  https://amazon.in

*** Test Cases ***
Amazon End to End
    Open Browser  ${url}  chrome
    Maximize Browser Window

    Wait Until Element Is Visible    xpath=//a[contains(text(), "Electronics")]
    Click Element    xpath=//a[contains(text(), "Electronics")]

#    Wait Until Element Is Visible    xpath=//input[@id="apb-browse-refinements-checkbox_5"]
    Click Element    xpath=(//i[@class="a-icon a-icon-checkbox"])[7]
    Sleep    3s

    Wait Until Element Is Visible    xpath=(//h2//span)[5]
    ${name}=    Get Text    xpath=(//h2//span)[5]
    Log To Console   ${name}

    Click Element    xpath=(//h2//span)[5]

    Switch Window    NEW

    Wait Until Page Contains    ${name}

    ${actual_price}=    Get Text    xpath=//span[@class='a-size-small aok-offscreen']
    Log To Console   Actual Price: ${actual_price}

    ${discount_price}=    Get Text    xpath=(//span[@class='a-price-whole'])[6]
    Log To Console   Discounted Price: ${discount_price}


    ${discount_percent}=    Get Text    xpath=//span[@class="apex-savings-container"]//child::span
    Log    Discount: ${discount_percent}

    Scroll Element Into View    xpath=//input[@id='add-to-cart-button']
    Click Button    add-to-cart-button

    Wait Until Element Is Visible    xpath=//span[@id='nav-cart-count']
    Click Element    xpath=//span[@id='nav-cart-count']

    Wait Until Page Contains    ${name}
    Log To Console  Product successfully added to cart

    Close Browser