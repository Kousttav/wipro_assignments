*** Settings ***
Library    SeleniumLibrary

Test Setup       Open Login Page
Test Teardown    Close Browser

*** Keywords ***
Open Login Page

    Open Browser
    ...    https://www.saucedemo.com/
    ...    chrome

    Input Text    id:user-name    standard_user
    Input Text    id:password     secret_sauce

    Click Button    id:login-button

*** Test Cases ***
Verify Inventory Page

    Location Should Contain
    ...    inventory.html