import pytest
from selene import browser


@pytest.mark.parametrize("desktop_browser", [(1920, 1080), (1280, 720)],
                         indirect=True)
def test_desktop_indirect(desktop_browser):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()


@pytest.mark.parametrize("mobile_browser", [(414, 896), (430, 932)],
                         indirect=True)
def test_mobile_indirect(mobile_browser):
    browser.open('/')
    browser.element('a[href="/login"].d-inline-flex').click()
