from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_FORM    = (By.CSS_SELECTOR, "#default")
    LOGIN_LINK    = (By.CSS_SELECTOR, "#login_link")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
