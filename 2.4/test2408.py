from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

opt = webdriver.ChromeOptions()
opt.add_experimental_option('w3c', False)
browser = webdriver.Chrome(chrome_options=opt)


browser.get("http://suninjuly.github.io/explicit_wait2.html")

#label_price = browser.find_element_by_id("price")

# говорим Selenium проверять в течение 15 секунд, пока цена не станет равной 10 000 руб
label = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '10000 RUR')
    )

button = browser.find_element_by_id("book")
button.click()

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

input_y = browser.find_element_by_id("answer")
input_y.send_keys(y)

button = browser.find_element_by_id("solve")
button.click()

alert2 = browser.switch_to.alert
alert2_text = alert2.text
print(alert2_text)
