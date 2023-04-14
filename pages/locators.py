from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    BASKET_LINK = (By.XPATH,
                   "//div[@class='basket-mini pull-right hidden-xs']/span/a")


class BasketPageLocators():
    PRODUCT_IN_BASKET = (By.ID, 'content_inner')


class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    EMAL_REGISTER = (By.NAME, 'registration-email')
    PASSWORD_REGISTER_FIRST = (By.NAME, 'registration-password1')
    PASSWORD_REGISTER_SECOND = (By.NAME, 'registration-password2')
    BUTTON_REGISTER = (By.NAME, 'registration_submit')
    EMAIL_LOGIN = (By.NAME, 'login-username')
    PASSWORD_LOGIN = (By.NAME, 'login-password')
    BUTTON_LOGIN = (By.NAME, 'login_submit')


class ProductPageLocators():
    BUTTON_ADD_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
    NAME_PRODUCT = (By.TAG_NAME, 'h1')
    PRICE_PRODUCT = (By.CSS_SELECTOR, 'p.price_color')
    NAME_PRODUCT_IN_BASKET = (By.XPATH, 
                              "//div[@id='messages']//div[1]/div[1]/strong")
    PRICE_IN_BASKET = (By.XPATH, "//div[@id='messages']//div[3]//p/strong")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='messages']/div[1]/div[1]")
