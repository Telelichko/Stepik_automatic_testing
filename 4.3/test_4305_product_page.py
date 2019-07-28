import pytest
from proj_4305_product_page import ProductPage
import time

product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

def test_guest_can_add_product_to_cart(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.add_product_to_cart()
    page.should_be_success_message()

def test_guest_get_correct_product_name_in_msg(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.add_product_to_cart()
    page.get_product_name_in_msg_success()

def test_guest_should_not_be_success_message(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.add_product_to_cart()
    page.should_not_be_success_message()

def test_guest_disappeared_element(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.add_product_to_cart()
    page.disappeared_element()