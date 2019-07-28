from proj_4308_product_page import ProductPage
from proj_4308_login_page import LoginPage
import pytest
import time


def test_message_disappeared_after_adding_product_to_cart(browser):
    product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, product_link)
    page.open()
    page.add_product_to_cart()
    page.should_be_disappeared_success_message()

def test_guest_can_add_product_to_cart(browser):
    product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, product_link)
    page.open()
    page.add_product_to_cart()
    page.should_be_success_message()

def test_guest_can_go_to_login_page_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_success_message(browser):
    product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, product_link)
    page.open()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, product_link)
    page.open()
    page.add_product_to_cart()
    page.should_not_be_success_message()

def test_guest_get_correct_product_name_in_msg(browser):
    product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, product_link)
    page.open()
    page.add_product_to_cart()
    page.get_product_name_in_msg_success()

def test_guest_should_see_login_link_on_product_page(browser):
    product_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, product_link)
    page.open()
    page.should_be_login_link()

