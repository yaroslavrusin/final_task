from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators():
    BUTTON_ADD_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
    NAME_PRODUCT = (By.TAG_NAME, 'h1')
    PRICE_PRODUCT = (By.CSS_SELECTOR, 'p.price_color')
    NAME_PRODUCT_IN_BASKET = (By.XPATH, 
                              "//div[@id='messages']//div[1]/div[1]/strong")
    PRICE_IN_BASKET = (By.XPATH, "//div[@id='messages']//div[3]//p/strong")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='messages']/div[1]/div[1]")
