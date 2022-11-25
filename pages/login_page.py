from .base_page import BasePage
from .locators  import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.should_be_register_form()

        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL), 'No register email input field present'
        el = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        el.send_keys(email)

        assert self.is_element_present(*LoginPageLocators.REGISTER_PASS1), 'No register password1 input field present'
        el = self.browser.find_element(*LoginPageLocators.REGISTER_PASS1)
        el.send_keys(password)

        assert self.is_element_present(*LoginPageLocators.REGISTER_PASS2), 'No register password2 input field present'
        el = self.browser.find_element(*LoginPageLocators.REGISTER_PASS2)
        el.send_keys(password)

        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), 'No register button present'
        el = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        el.click()
        print(f'User registered: [{email}/{password}]')

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'No login frame present'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'No register frame present'
