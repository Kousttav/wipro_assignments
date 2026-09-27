*** Settings ***
Library    RequestsLibrary

*** Test Cases ***
Verify API Response

    ${response}=    GET
    ...    https://jsonplaceholder.typicode.com/posts/1

    Should Be Equal As Strings
    ...    ${response.status_code}
    ...    200