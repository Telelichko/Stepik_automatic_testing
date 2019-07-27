﻿from selenium.common.exceptions import NoSuchElementException    # Импорт исключений

class BasePage(object):
    def __init__(self, browser, url, timeout=100):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)    # Команда для неявного ожидания в течении timeout сек.

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True