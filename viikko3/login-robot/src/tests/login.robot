*** Settings ***
Resource  resource.robot
*** Test Setup  Create User And Input Login Command ***

*** Test Cases ***
Login With Correct Credentials
    Create User And Input Login Command
    Input Credentials  kalle  kalle123
    Output Should Contain  Logged in

Login With Incorrect Password
    Create User And Input Login Command
    Input Credentials  kalle  kallo123
    Output Should Contain  Invalid username or password

Login with Nonexistent Username
    Create User And Input Login Command
    Input Credentials  joni  kalle123
    Output Should Contain  Invalid username or password

Register With Valid Username And Password
    Input New Command
    Input  joni
    Input  minijoni1
    Input Credentials  joni  minijoni1
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command
    Input Credentials  kalle  kalle123
    Input New Command
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input New Command
    Input Credentials  jo  minijoni1
    Output Should Contain  Username can only contain lowercase letters and must be at least 3 characters long

Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  joni  mini1
    Output Should Contain  Password must be at least 8 characters long and cannot contain only letters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  joni  minijonijimi
    Output Should Contain  Password must be at least 8 characters long and cannot contain only letters


*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123
    Input Login Command
    