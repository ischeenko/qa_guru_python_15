import pytest
from selene import browser


@pytest.fixture(params=[(1920, 1080), (1280, 720)])
def desktop_browser(request):
    browser.config.base_url = 'https://github.com'
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    yield

    browser.quit()


@pytest.fixture(params=[(414, 896), (430, 932)])
def mobile_browser(request):
    browser.config.base_url = 'https://github.com'
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    yield

    browser.quit()


@pytest.fixture(params=[(1920,1080), (1280,720), (414,896), (430,932)])
def browser_settings(request):
    browser.config.base_url = 'https://github.com'
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    if width > 900:
        yield "desktop"
    else:
        yield "mobile"


    browser.quit()