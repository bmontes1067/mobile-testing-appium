"""CartPage Android — shopping cart screen."""

from appium.webdriver.common.appiumby import AppiumBy
from pages.android.base_page import BasePage


class CartPage(BasePage):

    CART_TITLE      = (AppiumBy.XPATH, '//*[@text="Your Cart"]')
    CART_ITEMS      = (AppiumBy.ACCESSIBILITY_ID, "test-Item")
    ITEM_NAMES      = (AppiumBy.XPATH, '//android.widget.TextView[@content-desc="test-Item title"]')
    REMOVE_BUTTON   = (AppiumBy.ACCESSIBILITY_ID, "test-REMOVE")
    CHECKOUT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "test-CHECKOUT")
    CONTINUE_BTN    = (AppiumBy.ACCESSIBILITY_ID, "test-CONTINUE SHOPPING")
    EMPTY_CART_MSG  = (AppiumBy.XPATH, '//*[@text="No Items"]')

    def is_loaded(self) -> bool:
        return self.is_visible(self.CART_TITLE)

    def get_item_count(self) -> int:
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def get_item_names(self) -> list[str]:
        els = self.driver.find_elements(*self.ITEM_NAMES)
        return [el.text for el in els]

    def remove_first_item(self):
        self.click(self.REMOVE_BUTTON)

    def tap_checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    def tap_continue_shopping(self):
        self.click(self.CONTINUE_BTN)

    def is_empty(self) -> bool:
        return self.get_item_count() == 0
