from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/get_attribute.html"
browser.get(link)

x_element = browser.find_element_by_id("treasure")
x = x_element.get_attribute("valuex")
y = calc(x)

input = browser.find_element_by_id("answer")
input.send_keys(y)

checkbox1 = browser.find_element_by_id("robotCheckbox")
checkbox1.click()

radio1 = browser.find_element_by_id("robotsRule")
radio1.click()

button = browser.find_element_by_class_name("btn.btn-default")
button.click()
