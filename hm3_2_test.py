import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture()
def size_browser():
    browser.config.window_width = 1680
    browser.config.window_height = 1050

def test_open_browser(size_browser):
    browser.config.hold_browser_open = True
    browser.open('https://www.google.com/')
    browser.element('[name=q]').type('selene yashaka').press_enter()
    browser.element('#search').should(have.text('User-oriented Web UI browser tests'))
    pass

def test_negative_open_browser(size_browser):
    browser.config.hold_browser_open = True
    browser.open('https://www.google.com/')
    browser.element('[name=q]').type('sejhuyfgjhtriktruyjhjhgfi8u4erjkfolprtf14345').press_enter()
    browser.element('#search').should(have.text(''))
    pass



