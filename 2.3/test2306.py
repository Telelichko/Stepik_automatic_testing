from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

button = browser.find_element_by_class_name("trollface.btn.btn-primary")
button.click()

first_window = browser.window_handles[0]
second_window = browser.window_handles[1]
browser.switch_to.window(second_window)

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

input_y = browser.find_element_by_id("answer")
input_y.send_keys(y)

button = browser.find_element_by_class_name("btn.btn-primary")
button.click()

alert_finish = browser.switch_to.alert
alert_finish_text = alert_finish.text
print(alert_finish_text)