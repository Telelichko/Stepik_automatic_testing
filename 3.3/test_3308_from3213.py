from selenium import webdriver
import time

def input_values(link):
  browser = webdriver.Chrome()
  browser.get(link)

  input1 = browser.find_element_by_css_selector(".first_block>.first_class .form-control")
  input1.send_keys("Natalia")
  input1_text = input1.text

  input2 = browser.find_element_by_css_selector(".first_block>.second_class .form-control") 
  input2.send_keys("Telelichko")
  input2_text = input2.text

  input3 = browser.find_element_by_css_selector(".first_block>.third_class .form-control")
  input3.send_keys("tel@y.ru")
  input3_text = input3.text

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
  return welcome_text 

def test_Registration1():

  link = "http://suninjuly.github.io/registration1.html"
  welcome_text = input_values(link)

  assert welcome_text == "Поздравляем! Вы успешно зарегистировались!", "Should be equal text"

        
def test_Registration2():

  link = "http://suninjuly.github.io/registration2.html"
  welcome_text = input_values(link)

  assert welcome_text == "Поздравляем! Вы успешно зарегистировались!", "Should be equal text"

