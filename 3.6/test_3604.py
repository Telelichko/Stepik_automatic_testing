import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

#@pytest.fixture(scope="function")
#def browser(request):
#    browser_name = request.config.getoption("browser_name")
#    if browser_name == "firefox":
#        print("\nstart browser firefox for test...")
#        browser = webdriver.Firefox()
#    else:
#        print("\nstart browser chome for test...")
#        browser = webdriver.Chrome()
#    yield browser
#    print("\nquit browser...")
#    browser.quit()