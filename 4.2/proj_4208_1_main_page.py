from proj_4208_1_base_page import BasePage            # Импорт базового класса BasePage
from proj_4208_1_locators import MainPageLocators    # Импорт класса MainPageLocators
from selenium.webdriver.common.by import By
from proj_4208_1_login_page import LoginPage

class MainPage(BasePage):    # Создание класса MainPage, наследующего класс BasePage
    def go_to_login_page(self):    # Создание метода, позволяющего попасть на страницу авторитизации
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)


    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented" 


