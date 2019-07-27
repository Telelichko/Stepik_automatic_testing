from selenium import webdriver
import time
import math

def get_answer():
    answer = math.log(int(time.time()))
    return answer

link = "https://stepik.org/lesson/236895/step/1"
browser = webdriver.Chrome()
browser.get(link)
browser.implicitly_wait(15) # Настройка ожидания каждого элемента по 5 сек

textarea_answer = browser.find_element_by_css_selector(".textarea.ember-auto-resize")
input_answer = str(get_answer())
textarea_answer.send_keys(input_answer)

button_answer = browser.find_element_by_class_name("submit-submission")
button_answer.click()

output_answer = browser.find_element_by_css_selector(".smart-hints__hint")
output_answer_text = output_answer.text

assert output_answer_text == "Correct!", "Your answer isn't correct"