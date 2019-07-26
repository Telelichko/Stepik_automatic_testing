from proj_4205_base_page import BasePage    # Импорт базового класса BasePage 
from selenium.webdriver.common.by import By 

class MainPage(BasePage):    # Создание класса MainPage, наследующего класс BasePage
    def go_to_login_page(self):    # Создание метода, позволяющего попасть на страницу авторитизации
        link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented" 


