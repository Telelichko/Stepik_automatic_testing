from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

button = browser.find_element_by_class_name("btn.btn-primary")
button.click()

confirm = browser.switch_to.alert
confirm.accept()

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

input_y = browser.find_element_by_id("answer")
input_y.send_keys(y)

button = browser.find_element_by_class_name("btn.btn-primary")
button.click()

alert2 = browser.switch_to.alert
alert2_text = alert2.text
print(alert2_text)
