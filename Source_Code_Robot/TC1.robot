*** Settings ***
Library     SeleniumLibrary
Suite Setup  Open browser    ${URL}   ${BROWSER}
Suite Teardown  Close All Browsers

*** Variables ***
${browser}  chrome
${url}  https://www.expedia.com/

*** Test Cases ***
Test Expedia
    testOpen
    testLeaving
    testGoing
    testDay
    testCheck
    testData

*** Keywords ***
testOpen
    maximize browser window
    sleep   2
    click element   xpath://div[contains(text(),'More travel')]
    click link   Flights
    sleep   2
    [Tags]  TC1

testLeaving
    click element   xpath://button[contains(@aria-label,'Leaving from')]
    input text  xpath://input[contains(@placeholder,'Where are you leaving from?')]  Hanoi
    click element   xpath://button[contains(@data-stid,'location-field-leg1-origin-result-item-button')]
    sleep   2

testGoing
    click element   xpath://button[contains(@aria-label,'Going to')]
    input text  xpath://input[contains(@placeholder,'Where are you going to?')]     Ho Chi Minh
    click element   xpath://button[contains(@data-stid,'location-field-leg1-destination-result-item-button')]
    sleep   2

testDay
    click element   id:d1-btn
    sleep   1
    click element   xpath://button[contains(@aria-label,'Oct 1, 2021')]
    sleep   1
    click element   xpath://button[contains(@data-stid,'apply-date-picker')]
    sleep   2


testCheck
    click element   xpath://button[contains(text(),'Search')]
    sleep   2

testData
    click element   xpath://*[@id="app-layer-base"]/div[2]/div[3]/div/section/main/div[1]/div/button
    ${flights}=  Get Text    xpath://table[contains(@role,'table')]
    Should Not Be Empty     ${flights}
    Log To Console    ${flights}

    Log To Console  =========================
    ${Length}=  Get Element Count     xpath://li[contains(@data-test-id,'offer-listing')]
	Log To Console  ${Length}
	Log To Console  =========================
	FOR     ${i}  IN RANGE  1   ${Length}
	    ${ListText}=    Get Text    xpath://li[${i}]
        Log To Console  ${ListText}
    END

	Log To Console  =========================
	Log To Console  Finish test

