from .pages.product_page import ProductPage

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

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = get_product_page(browser, link)
    product_page.click_button_add_basket()
    product_page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    product_page = get_product_page(browser, link)
    product_page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = get_product_page(browser, link)
    product_page.click_button_add_basket()
    product_page.should_be_disappeared_success_message()
