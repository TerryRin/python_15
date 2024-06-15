import pytest
from selene import browser


@pytest.fixture()
def setting_browser_desktop():
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    browser.quit()


@pytest.fixture()
def setting_browser_mobile():
    browser.config.window_width = 430
    browser.config.window_height = 932

    yield

    browser.quit()


@pytest.fixture(params=['desktop', 'mobile'])
def driver(request):
    if request.param == 'desktop':
        browser.config.window_width = 1920
        browser.config.window_height = 1080
    else:
        browser.config.window_width = 430
        browser.config.window_height = 932

    yield

    browser.quit()


@pytest.fixture(params=[(1920, 1080), (430, 932)])
def driver_setup(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
