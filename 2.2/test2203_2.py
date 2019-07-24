from selenium import webdriver
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

select = browser.find_element_by_tag_name("select").click()
select.find_element_by_css_selector("[value={}]").Format(y).click()

button = browser.find_element_by_class_name("btn.btn-default")
button.click()