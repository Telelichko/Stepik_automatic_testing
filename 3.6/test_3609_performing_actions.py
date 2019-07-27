import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/catalogue/"
browser = webdriver.Chrome()
browser.get(link)

#a_href = browser.find_element_by_xpath("//article[@class='product_pod']//a[0]") # Выбор элемента ссылочного типа
#a_href = browser.find_element_by_css_selector(".product_pod a") 
#a_href = browser.find_element_by_css_selector(".row article.product_pod[2] a") 
#a_href = browser.find_element_by_css_selector("col-xs-6.col-sm-4.col-md-3.col-lg-3>.product_pod:nth-child(2) a") 
#a_href = browser.find_element_by_css_selector(".product_pod:nth-child(0) a")
#a_href = browser.find_element_by_css_selector(".col-xs-6.col-sm-4.col-md-3.col-lg-3:nth-child(0) a")
#a_href = browser.find_element_by_css_selector(".form-horizontal li:nth-child(0)")
#a_href = browser.find_element_by_css_selector(".form-horizontal .row:first-child a")

a_href = browser.find_element_by_css_selector("product_pod:nth-child(0)")

a_href.click()

