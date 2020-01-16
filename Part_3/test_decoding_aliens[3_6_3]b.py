import time
import math
import pytest
from selenium import webdriver



#fixture, initializing browser and cleaning up after the tests?

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    
@pytest.mark.parametrize('lesson_link', [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905])
def test_parametrize_lesson_link(browser, lesson_link):
    link = f"https://stepik.org/lesson/{lesson_link}/step/1"

    #open browser
    browser.get(link)
    time.sleep(3)
    answer_field = browser.find_element_by_css_selector('[class="textarea string-quiz__textarea ember-text-area ember-view"]')
    time.sleep(3)
    

