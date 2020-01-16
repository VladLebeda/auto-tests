import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.aliens_decode    
@pytest.mark.parametrize('lesson_link', [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905])
def test_parametrize_lesson_link(browser, lesson_link):
    link = f"https://stepik.org/lesson/{lesson_link}/step/1"

    #open browser
    browser.get(link)
    
    #waiting untill textarea field is loaded
    element1 = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.TAG_NAME, "textarea")))  
    answer_field = browser.find_element_by_css_selector('[class="textarea string-quiz__textarea ember-text-area ember-view"]')
    
    #calculating current answer and sending it to the answer field
    answer = math.log(int(time.time()))
    answer_field.send_keys(str(answer))
    
    #finding send button
    answer_button = browser.find_element_by_css_selector('[class="submit-submission"]')
    answer_button.click()
    
    #waiting for page to load after submitting an answer
    element2 = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.TAG_NAME, "pre")))
    
    #check if the text == "Correct!"
    success_field = browser.find_element_by_css_selector('[class="smart-hints__hint"]').text
    assert success_field == "Correct!", "Incorrect answer!"
    
