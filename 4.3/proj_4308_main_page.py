from proj_4308_base_page import BasePage            # Импорт базового класса BasePage
from proj_4308_locators import MainPageLocators    # Импорт класса MainPageLocators


class MainPage(BasePage):    # Создание класса MainPage, наследующего класс BasePage
    def __init__(self, *args, **kwargs): # Заглушка
        super(MainPage, self).__init__(*args, **kwargs)

