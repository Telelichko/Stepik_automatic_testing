﻿from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)

# Заполняем все поля
input1 = browser.find_element_by_xpath("//div[@class='first_block']//div[@class='form-group first_class']//input")
input1.send_keys("Ivan")
input2 = browser.find_element_by_xpath("//div[@class='first_block']//div[@class='form-group second_class']//input")
input2.send_keys("Petrov")
input3 = browser.find_element_by_xpath("//div[@class='first_block']//div[@class='form-group third_class']//input")
input3.send_keys("test@test.test")
input4 = browser.find_element_by_xpath("//div[@class='second_block']//div[@class='form-group first_class']//input")
input4.send_keys("1234567890")
input5 = browser.find_element_by_xpath("//div[@class='second_block']//div[@class='form-group second_class']//input")
input5.send_keys("Russia")

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
