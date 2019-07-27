from selenium import webdriver

def get_link():
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    return link


def test_should_be_button_basket(browser):
    link = get_link()
    browser.get(link)
    assert browser.find_element_by_css_selector("button.btn-add-to-basket")


 