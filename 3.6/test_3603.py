import pytest
from selenium import webdriver
import time
import math

def get_answer():
    answer = math.log(int(time.time()))
    return answer

#@pytest.fixture(scope="function")
#def browser():
#    print("\nstart browser for test..")
#    #browser = webdriver.Chrome()

#    browser_name = request.config.getoption("browser_name")
#    if browser_name == "firefox":

#    driver = webdriver.Firefox()
#    browser.implicitly_wait(15) # Настройка ожидания каждого элемента по 5 сек
#    yield browser
#    print("\nquit browser..")
#    browser.quit()

@pytest.mark.parametrize('lastnum', ["895", "896", "897", "898", "899", "903", "904", "905"])
# 4, 5, 7 
#@pytest.mark.parametrize('lastnum', ["895" ])
def test_guest_should_see_login_link(browser, lastnum):
    link = "https://stepik.org/lesson/236{}/step/1".format(lastnum)
    browser.get(link)

    textarea_answer = browser.find_element_by_css_selector(".textarea.ember-auto-resize")
    answer = str(get_answer())
    textarea_answer.send_keys(answer)

    button_answer = browser.find_element_by_class_name("submit-submission")
    button_answer.click()

    output_answer = browser.find_element_by_css_selector(".smart-hints__hint")
    output_answer_text = output_answer.text
        
    assert output_answer_text == "Correct!", output_answer_text

