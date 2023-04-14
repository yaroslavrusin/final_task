from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_not_products_in_basket(self):
        text_in_basket = self.browser.find_element(*BasketPageLocators.PRODUCT_IN_BASKET).text
        print(text_in_basket)
        assert text_in_basket == 'Your basket is empty. Continue shopping', \
            'Product in the basket'
