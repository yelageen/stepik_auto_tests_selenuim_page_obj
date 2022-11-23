from .base_page import BasePage
from .locators  import ProductPageLocators

class ProductPage(BasePage): 
    def add_to_basket(self):
        # get product title incription
        assert self.is_element_present(*ProductPageLocators.PRODUCT_TITLE), 'No product title incription presents'
        pTitle = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text

        # get product price incription
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), 'No product price incription presents'
        pPrice = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

        # click add to basket button
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), 'No "Add to basket" button presents'
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()
        self.solve_quiz_and_get_code()

        # get product title incription from message
        assert self.is_element_present(*ProductPageLocators.MESSAGE_TITLE), 'No product title incription presents'
        mTitle = self.browser.find_element(*ProductPageLocators.MESSAGE_TITLE).text

        # get product price incription from message
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRICE), 'No product price incription presents'
        mPrice = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE).text

        # check both title and price are the same
        assert pTitle == mTitle, f'Added "{mTitle}" item. Tried to add the "{pTitle}" one'
        assert pPrice == mPrice, f'Added item at "{mPrice}" price. Tried to add the item at "{pPrice}" one'
        print(f'Added "{mTitle}" item at "{mPrice}" price.')

    def should_disappear_message_title(self):
        assert self.is_element_disappeared(*ProductPageLocators.MESSAGE_TITLE), "The message with the title should disappear but it doesn't"

    def should_not_be_message_title(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_TITLE), 'The message with the title should not appear but it does'
