from proj_4303_product_page import ProductPage

product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

def test_guest_can_add_product_to_cart(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.add_product_to_cart()

def test_guest_get_correct_product_name_in_msg(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.add_product_to_cart()
    product_page = ProductPage(browser, browser.current_url)
    product_name = product_page.get_product_name()
    mag_product = product_page.get_msg_product()
    assert product_name in mag_product, "Message does not contain product name"










