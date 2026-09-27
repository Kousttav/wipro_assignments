*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://www.saucedemo.com/

*** Test Cases ***
Open Browser And Navigate
    Open Browser    ${URL}    chrome
    Maximize Browser Window

    Input Text    id:user-name    standard_user
    Input Text    id:password     secret_sauce

    Page Should Contain Element    id:login-button

    Close Browser
    