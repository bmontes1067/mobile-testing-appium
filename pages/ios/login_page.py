"""LoginPage iOS — My Demo App (Sauce Labs)."""

from appium.webdriver.common.appiumby import AppiumBy
from pages.ios.base_page import BasePage


class LoginPage(BasePage):

    USERNAME_FIELD = (AppiumBy.ACCESSIBILITY_ID, "test-Username")
    PASSWORD_FIELD = (AppiumBy.ACCESSIBILITY_ID, "test-Password")
    LOGIN_BUTTON   = (AppiumBy.ACCESSIBILITY_ID, "test-LOGIN")
    ERROR_MESSAGE  = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Username and password do not match any user in this service."]')
    USERNAME_ERROR = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Username is required"]')

    def login(self, username: str, password: str):
        self.type_text(self.USERNAME_FIELD, username)
        self.type_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)

    def is_username_error_shown(self) -> bool:
        return self.is_visible(self.USERNAME_ERROR)
