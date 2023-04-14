from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.click_button_add_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_product_in_basket()
    product_page.shold_be_price_in_basket()
