from selenium.webdriver.common.by import By

class BasePageLocators():
    BASKET_BUTTON      = (By.CSS_SELECTOR, ".basket-mini > span > .btn")
    LOGIN_LINK         = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON          = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_EMPTY       = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_TITLE       = (By.CSS_SELECTOR, "#content_inner > .basket-title")

class LoginPageLocators():
    LOGIN_FORM         = (By.CSS_SELECTOR, '#default')
    REGISTER_BUTTON    = (By.CSS_SELECTOR, '[name="registration_submit"]')
    REGISTER_EMAIL     = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_FORM      = (By.CSS_SELECTOR, '#register_form')
    REGISTER_PASS1     = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_PASS2     = (By.CSS_SELECTOR, '#id_registration-password2')

class MainPageLocators():
    pass

class ProductPageLocators():
    ADD_TO_BASKET      = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    MESSAGE_PRICE      = (By.XPATH, '//*[@id="messages"]/div[3]//strong')
    MESSAGE_TITLE      = (By.XPATH, '//*[@id="messages"]/div[1]//strong')
    PRODUCT_PRICE      = (By.XPATH, '//*[@id="content_inner"]//p')
    PRODUCT_TITLE      = (By.XPATH, '//*[@id="content_inner"]//h1')
