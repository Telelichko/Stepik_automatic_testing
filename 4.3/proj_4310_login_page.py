from proj_4310_base_page import BasePage            # Импорт базового класса BasePage
from proj_4310_locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert str(self.browser.current_url) == "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        #assert self.is_element_present(*LoginPageLocators.LOGIN_URL), "Login url is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
