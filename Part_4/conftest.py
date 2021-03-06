import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help='Current page language - fr, ru, eu-gb etc etc')


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name').lower()
    user_language = request.config.getoption('language').lower()

    if browser_name == 'chrome':
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)

    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    print(f"\nStarting {browser_name.capitalize()} browser.")
    yield browser

    print('\nquit browser..')
    browser.quit()
