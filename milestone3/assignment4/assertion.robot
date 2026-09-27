*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Verify Login

    Open Browser
    ...    https://www.saucedemo.com/
    ...    chrome

    Input Text    id:user-name    standard_user
    Input Text    id:password     secret_sauce

    Click Button    id:login-button

    Location Should Contain
    ...    inventory.html

    Close Browser