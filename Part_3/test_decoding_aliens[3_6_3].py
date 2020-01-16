import time
import math
import selenium

answer = math.log(int(time.time()))




#open browser



#input answer


#send answer

#wait for feedback


#check if the text == "Correct!"


https://stepik.org/lesson/236895/step/1
https://stepik.org/lesson/236896/step/1
https://stepik.org/lesson/236897/step/1
https://stepik.org/lesson/236898/step/1
https://stepik.org/lesson/236899/step/1
https://stepik.org/lesson/236903/step/1
https://stepik.org/lesson/236904/step/1
https://stepik.org/lesson/236905/step/1





try:
    browser = webdriver.Chrome()
    browser.get(link)
    answer_field = browser.find_element_by_css_selector('[class="textarea string-quiz__textarea ember-text-area ember-view"]')
    #calculating current answer and sending it to the answer field
    answer = math.log(int(time.time()))
    answer_field.send_keys(answer)
    #finding send button
    answer_button = browser.find_element_by_css_selector('[class="submit-submission"]')
    answer_button.click()

#textarea
    find_by_css_selector('[class="smart-hints__hint"]')
    
