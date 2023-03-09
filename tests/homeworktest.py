from selene.support.shared import browser
from selene import be, have
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
    browser.element('#firstName').should(be.blank).type('Антон')
    browser.element('#lastName').should(be.blank).type('Антонов')
    browser.element('#userEmail').should(be.blank).type('anton@anton.ru')

