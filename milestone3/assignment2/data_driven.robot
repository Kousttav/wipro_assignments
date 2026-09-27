*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://www.saucedemo.com/
${USERNAME}    standard_user
${PASSWORD}    secret_sauce

*** Test Cases ***
Login Test
    Open Browser    ${URL}    chrome

    Input Text    id:user-name    ${USERNAME}
    Input Text    id:password     ${PASSWORD}

    Click Button    id:login-button

    Close Browser