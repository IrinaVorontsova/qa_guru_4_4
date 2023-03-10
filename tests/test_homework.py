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
    first_name = 'Антон'
    last_name = 'Антонов'
    email = 'anton@anton.ru'
    phone = '7111111111'
    hobby = 'Computer Science'
    address = 'USA, 12723 street'
    photo_path = 'photo_test.jpg'


    browser.element('#firstName').should(be.blank).type(first_name)
    browser.element('#lastName').should(be.blank).type(last_name)
    browser.element('#userEmail').should(be.blank).type(email)
    browser.element('[for="gender-radio-3"]').should(have.text('Other')).click()
    browser.element('#userNumber').should(be.blank).type(phone)

    browser.element('#dateOfBirthInput').click()
    browser.element(
        'select[class="react-datepicker__month-select"] option[value="10"]').click()
    browser.element(
        'select[class="react-datepicker__year-select"] option[value="2000"]').click()
    browser.element(
        '*[class="react-datepicker__day react-datepicker__day--020"]').click()

    browser.element('#subjectsInput').should(be.blank).type(hobby).press_enter()
    browser.element('[for="hobbies-checkbox-1"]').should(have.text('Sports')).click()

    browser.element('#uploadPicture').send_keys(os.getcwd() + "/" + photo_path)

    browser.element('#currentAddress').should(be.blank).type(address)

    browser.element('#react-select-3-input').should(be.blank).type('Rajasthan').press_enter()
    browser.element('#react-select-4-input').should(be.blank).type('Jaiselmer').press_enter()
    browser.element('#submit').perform(command.js.click)

    #Проверка
    browser.element('//tr[1]/td[2]').should(have.text(first_name + ' ' + last_name))
    browser.element('//tr[2]/td[2]').should(have.text(email))
    browser.element('//tr[3]/td[2]').should(have.text('Other'))
    browser.element('//tr[4]/td[2]').should(have.text(phone))
    browser.element('//tr[5]/td[2]').should(have.text('20 November,2000'))
    browser.element('//tr[6]/td[2]').should(have.text(hobby))
    browser.element('//tr[7]/td[2]').should(have.text('Sports'))
    browser.element('//tr[8]/td[2]').should(have.text(photo_path))
    browser.element('//tr[9]/td[2]').should(have.text(address))
    browser.element('//tr[10]/td[2]').should(have.text('Rajasthan Jaiselmer'))
    browser.element('#closeLargeModal').perform(command.js.click)