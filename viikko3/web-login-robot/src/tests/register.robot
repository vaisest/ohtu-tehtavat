*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page
Test Teardown  Reset Application

*** Test Cases ***
Register With Valid Username And Password
    Go To Register Page
    Set Username  joni
    Set Password  minijoni123
    Set Confirmation  minijoni123
    Submit Credentials
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Go To Register Page
    Set Username  j
    Set Password  minijoni123
    Set Confirmation  minijoni123
    Submit Credentials
    Register Should Fail With Message  Username can only contain lowercase letters and must be at least 3 characters long

Register With Valid Username And Too Short Password
    Go To Register Page
    Set Username  joni
    Set Password  m1
    Set Confirmation  m1
    Submit Credentials
    Register Should Fail With Message  Password must be at least 8 characters long and cannot contain only letters

Register With Nonmatching Password And Password Confirmation
    Go To Register Page
    Set Username  joni
    Set Password  minijoni1
    Set Confirmation  minijami1
    Submit Credentials
    Register Should Fail With Message  Password and password confirmation not equal

Login After Successful Registration
    Go To Register Page
    Set Username  joni
    Set Password  minijoni123
    Set Confirmation  minijoni123
    Submit Credentials
    Welcome Page Should Be Open
    Go To Ohtu Page
    Click Button  Logout
    Set Username  joni
    Set Password  minijoni123
    Click Button  Login
    Main Page Should Be Open

Login After Failed Registration
    Go To Register Page
    Set Username  j
    Set Password  minijoni123
    Set Confirmation  minijoni123
    Submit Credentials
    Register Should Fail With Message  Username can only contain lowercase letters and must be at least 3 characters long
    Go To Login Page
    Set Username  j
    Set Password  minijoni123
    Click Button  Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}
    