from selenium.webdriver.common.by import By

class BasePageLocators():
    BASKET_BUTTON      = (By.CSS_SELECTOR, ".basket-mini > span > .btn")
    LOGIN_LINK         = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class BasketPageLocators():
    BASKET_TITLE       = (By.CSS_SELECTOR, "#content_inner > .basket-title")
    BASKET_EMPTY       = (By.CSS_SELECTOR, "#content_inner > p")

class LoginPageLocators():
    LOGIN_FORM         = (By.CSS_SELECTOR, '#default')
    REGISTER_FORM      = (By.CSS_SELECTOR, '#register_form')

class MainPageLocators():
    pass

class ProductPageLocators():
    ADD_TO_BASKET      = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    MESSAGE_PRICE      = (By.XPATH, '//*[@id="messages"]/div[3]//strong')
    MESSAGE_TITLE      = (By.XPATH, '//*[@id="messages"]/div[1]//strong')
    PRODUCT_PRICE      = (By.XPATH, '//*[@id="content_inner"]//p')
    PRODUCT_TITLE      = (By.XPATH, '//*[@id="content_inner"]//h1')
