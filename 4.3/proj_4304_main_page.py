﻿from proj_4304_base_page import BasePage            # Импорт базового класса BasePage
from proj_4304_locators import MainPageLocators    # Импорт класса MainPageLocators

class MainPage(BasePage):    # Создание класса MainPage, наследующего класс BasePage
    def go_to_login_page(self):    # Создание метода, позволяющего попасть на страницу авторитизации
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        alert = self.browser.switch_to.alert
        alert.accept()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented" 


