import pytest
import selenium
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.language_test
def test_add_to_the_cart_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)  # We get browser language via prefs or intl from browser(request) fixture

    #time.sleep(30)  # For testing purposes

    # Waiting for the page to fully load
    element = WebDriverWait(browser, 20).until(ec.presence_of_element_located((By.TAG_NAME, 'button')))

    # Asserting that "Add to the cart" button is present
    add_to_cart_button = browser.find_elements_by_css_selector('[class="btn btn-lg btn-primary btn-add-to-basket"]')
    assert add_to_cart_button is not None, 'No add to the cart button is found!'