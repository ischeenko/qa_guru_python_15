from selene import browser
import pytest


def test_desktop_skip(browser_settings):
    if browser_settings == "desktop":
        browser.open('/')
        browser.element('.HeaderMenu-link--sign-in').click()

    else:
        pytest.skip(reason='Это мобильное разрешение')

def test_mobile_skil(browser_settings):
    if browser_settings == "mobile":
        browser.open('/')
        browser.element('a[href="/login"].d-inline-flex').click()

    else:
        pytest.skip(reason='Это десктопное разрешение ')




