"""CheckoutPage iOS."""

from appium.webdriver.common.appiumby import AppiumBy
from pages.ios.base_page import BasePage


class CheckoutPage(BasePage):

    FIRST_NAME_FIELD = (AppiumBy.ACCESSIBILITY_ID, "test-First Name")
    LAST_NAME_FIELD  = (AppiumBy.ACCESSIBILITY_ID, "test-Last Name")
    ZIP_FIELD        = (AppiumBy.ACCESSIBILITY_ID, "test-Zip/Postal Code")
    CONTINUE_BUTTON  = (AppiumBy.ACCESSIBILITY_ID, "test-CONTINUE")
    FINISH_BUTTON    = (AppiumBy.ACCESSIBILITY_ID, "test-PLACE ORDER")
    SUCCESS_TITLE    = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Checkout Complete"]')

    def fill_form(self, first_name: str, last_name: str, zip_code: str):
        self.type_text(self.FIRST_NAME_FIELD, first_name)
        self.type_text(self.LAST_NAME_FIELD, last_name)
        self.type_text(self.ZIP_FIELD, zip_code)

    def tap_continue(self):
        self.click(self.CONTINUE_BUTTON)

    def tap_finish(self):
        self.click(self.FINISH_BUTTON)

    def is_order_complete(self) -> bool:
        return self.is_visible(self.SUCCESS_TITLE)
