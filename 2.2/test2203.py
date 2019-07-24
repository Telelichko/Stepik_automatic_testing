from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/selects1.html"
browser.get(link)

value1_element = browser.find_element_by_id("num1") 
value1 = value1_element.text
value2_element = browser.find_element_by_id("num2")
value2 = value2_element.text

y_int = int(value1) + int(value2)
y = str(y_int)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(y)

button = browser.find_element_by_class_name("btn.btn-default")
button.click()