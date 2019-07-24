from selenium import webdriver
import math

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html" # Initialization variable link
browser.get(link) # Open page
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

input = browser.find_element_by_id("answer")
input.send_keys(y)

button = browser.find_element_by_tag_name("button") # Find button
browser.execute_script("return arguments[0].scrollIntoView(true);", button) # Scroll page

checkbox1 = browser.find_element_by_id("robotCheckbox")
checkbox1.click()

radio1 = browser.find_element_by_id("robotsRule")
radio1.click()

button.click() # Click button
assert True