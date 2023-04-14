from selenium.common.exceptions import NoSuchElementException
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert "login" in url, "'login' not in current page url"

    def should_be_login_form(self):
        try:
            self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        except NoSuchElementException:
            assert False, "Missing login form"

    def should_be_register_form(self):
        try:
            self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        except NoSuchElementException:
            assert False, "Missing register_form"
