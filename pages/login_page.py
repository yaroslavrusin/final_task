from selenium.common.exceptions import NoSuchElementException
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_login = self.browser.find_element(*LoginPageLocators.EMAL_REGISTER)
        email_login.send_keys(email)
        password_login_first = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTER_FIRST)
        password_login_first.send_keys(password)
        password_login_second = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTER_SECOND)
        password_login_second.send_keys(password)
        button_register = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER)
        button_register.click()

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
