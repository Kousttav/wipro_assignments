*** Settings ***
Library    Calculator.py

*** Test Cases ***
Sum Test

    ${result}=    Calculate Sum    10    20

    Should Be Equal As Integers
    ...    ${result}
    ...    30