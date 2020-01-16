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
def test_parametrize_lesson_link(browser, 'lesson_link'):
    link = f"https://stepik.org/lesson/{lesson_link}/step/1"

    #open browser
    browser.get(link)
    answer_field = browser.find_element_by_css_selector('[class="textarea string-quiz__textarea ember-text-area ember-view"]')

    #calculating current answer and sending it to the answer field
    answer = math.log(int(time.time()))
    answer_field.send_keys(answer)

    #finding send button
    answer_button = browser.find_element_by_css_selector('[class="submit-submission"]')
    answer_button.click()

    #waiting for loading
    time.sleep(1)

    #check if the text == "Correct!"
    success_field = browser.find_by_css_selector('[class="smart-hints__hint"]').text
    assert success_field == "Correct!", "Incorrect answer!"
