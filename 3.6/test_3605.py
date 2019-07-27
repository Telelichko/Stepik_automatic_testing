import pytest
from selenium import webdriver

# Не работает

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "firefox": 
        print("\nstart browser firefox for test...")
        fp = webdriver.FirefoxProfile()
        browser = webdriver.Firefox(firefox_profile=fp)
    else browser_name == "chrome":
        print("\nstart browser chrome for test...")
        options = Options()
        browser = webdriver.Chrome(options=options)    
    yield browser
    print("\nquit browser..")
    browser.quit()

def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")


 