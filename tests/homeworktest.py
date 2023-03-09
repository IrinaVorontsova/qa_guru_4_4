from selene.support.shared import browser
from selene import be, have, command
import pytest
import os


@pytest.fixture()
def driver_browser():
    browser.config.window_width = 1600
    browser.config.window_height = 1024
    browser.open('https://demoqa.com/automation-practice-form')
    yield driver_browser
    browser.close()


def test_form(driver_browser):
    FIRST_NAME = 'Антон'
    LAST_NAME = 'Антонов'
    EMAIL = 'anton@anton.ru'
    PHONE = '7111111111'
    HOBBY = 'Cosplay'
    ADDRESS = 'USA, 12723 street'
    PHOTO_PATH = 'photo_test.jpg'


    browser.element('#firstName').should(be.blank).type(FIRST_NAME)
    browser.element('#lastName').should(be.blank).type(LAST_NAME)
    browser.element('#userEmail').should(be.blank).type(EMAIL)
    browser.element('[for="gender-radio-3"]').should(have.text('Other')).click()
    browser.element('#userNumber').should(be.blank).type(PHONE)

    browser.element('#dateOfBirthInput').click()
    browser.element(
        'select[class="react-datepicker__month-select"] option[value="10"]').click()
    browser.element(
        'select[class="react-datepicker__year-select"] option[value="2000"]').click()
    browser.element(
        '*[class="react-datepicker__day react-datepicker__day--020"]').click()

    browser.element('#subjectsInput').should(be.blank).type(HOBBY)
    browser.element('[for="hobbies-checkbox-1"]').should(have.text('Sports')).click()

    browser.element('#uploadPicture').send_keys(os.getcwd() + "/" + PHOTO_PATH)

    browser.element('#currentAddress').should(be.blank).type(ADDRESS)

    browser.element('#react-select-3-input').should(be.blank).type('Rajasthan').press_enter()
    browser.element('#react-select-4-input').should(be.blank).type('Jaiselmer').press_enter()
    browser.element('#submit').perform(command.js.click)

    #Проверка
    browser.element('//tr[1]/td[2]').should(have.text(FIRST_NAME + ' ' + LAST_NAME))
    browser.element('//tr[2]/td[2]').should(have.text(EMAIL))
    browser.element('//tr[3]/td[2]').should(have.text('Other'))
    browser.element('//tr[4]/td[2]').should(have.text(PHONE))
    browser.element('//tr[5]/td[2]').should(have.text('20 November,2000'))
    browser.element('//tr[6]/td[2]').should(have.text(''))
    browser.element('//tr[7]/td[2]').should(have.text('Sports'))
    browser.element('//tr[8]/td[2]').should(have.text(PHOTO_PATH))
    browser.element('//tr[9]/td[2]').should(have.text(ADDRESS))
    browser.element('//tr[10]/td[2]').should(have.text('Rajasthan Jaiselmer'))
    browser.element('#closeLargeModal').perform(command.js.click)