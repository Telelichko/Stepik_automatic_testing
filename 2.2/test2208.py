from selenium import webdriver
import os 

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

input_fname = browser.find_element_by_name("firstname")
input_fname.send_keys("Имя")
input_lname = browser.find_element_by_name("lastname")
input_lname.send_keys("Фамилия")
input_email = browser.find_element_by_name("email")
input_email.send_keys("Почта")

current_dir = os.path.abspath(os.path.dirname(__file__)) # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file2208.txt') # добавляем к этому пути имя файла 
button_file = browser.find_element_by_id("file")
button_file.send_keys(file_path)

button_submit = browser.find_element_by_class_name("btn.btn-primary")
button_submit.click()
