from selenium import webdriver

browser = webdriver.Chrome()

# ���������� ��� �����
# ��������� �������� ������� ������
# ������ ���� �� ����������, ���� ��� �������� ������ ��� �������
browser.get("https://fake-shop.com/book1.html")

# ��������� ����� � �������
add_button = browser.find_element_by_css_selector(".add")
add_button.click()

# ��������� �������� ������� ������
browser.get("https://fake-shop.com/book2.html")

# ��������� ����� � �������
add_button = browser.find_element_by_css_selector(".add")
add_button.click()

# �������� ��������
# ��������� �������
browser.get("https://fake-shop.com/basket.html")

# ���� ��� ����������� ������
goods = browser.find_elements_by_css_selector(".good")

# ���������, ��� ���������� ������� ����� 2
assert len(goods) == 2