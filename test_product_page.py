import pytest
from .pages.product_page import ProductPage
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def get_product_page(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    return product_page


def test_guest_can_add_product_to_basket(browser):
    product_page = get_product_page(browser, link)
    product_page.click_button_add_basket()
    product_page.should_be_product_in_basket()
    product_page.shold_be_price_in_basket()


@pytest.mark.xfail(strict=True, run=False)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = get_product_page(browser, link)
    product_page.click_button_add_basket()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    product_page = get_product_page(browser, link)
    product_page.should_not_be_success_message()


@pytest.mark.xfail(strict=True, run=False)
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = get_product_page(browser, link)
    product_page.click_button_add_basket()
    product_page.should_be_disappeared_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com//en-gb/catalogue/'
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.go_to_basket_page()
    basket_page = BasketPage(main_page.browser, main_page.browser.current_url)
    basket_page.should_be_not_products_in_basket()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_basket_page()
    basket_page = BasketPage(product_page.browser, product_page.browser.current_url)
    basket_page.should_be_not_products_in_basket()
