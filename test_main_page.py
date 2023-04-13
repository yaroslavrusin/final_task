from selenium import webdriver
from selenium.webdriver.common.by import By

LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_add_cart_button(browser: webdriver.Chrome):
    browser.get(LINK)
    button_add_cart = browser.find_elements(By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket')
    assert len(button_add_cart) == 1, 'Missing add to cart button'
