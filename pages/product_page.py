from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_button_add_basket(self):
        button_add_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_BASKET)
        button_add_basket.click()

    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        return product_name.text

    def get_price_product(self):
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)
        return price_product.text

    def get_product_name_in_basket(self):
        name_in_basket = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_IN_BASKET)
        return name_in_basket.text

    def get_price_in_basket(self):
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET)
        return price_in_basket.text

    def should_be_product_in_basket(self):
        product_name = self.get_product_name()
        name_in_basket = self.get_product_name_in_basket()
        assert product_name == name_in_basket, "Wrong product added to basket"

    def shold_be_price_in_basket(self):
        price_product = self.get_price_product()
        price_in_basket = self.get_price_in_basket()
        assert price_product == price_in_basket, "The price in the basket does not match the price of the product"
