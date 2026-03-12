"""
LoginPage Android — My Demo App (Sauce Labs)
Selectors obtained with Appium Inspector on the official APK.
"""

from appium.webdriver.common.appiumby import AppiumBy
from pages.android.base_page import BasePage


class LoginPage(BasePage):

    # ─── Locators ─────────────────────────────────────────────────────────────
    USERNAME_FIELD = (AppiumBy.ACCESSIBILITY_ID, "test-Username")
    PASSWORD_FIELD = (AppiumBy.ACCESSIBILITY_ID, "test-Password")
    LOGIN_BUTTON   = (AppiumBy.ACCESSIBILITY_ID, "test-LOGIN")
    ERROR_MESSAGE  = (AppiumBy.XPATH, '//android.widget.TextView[@text="Username and password do not match any user in this service."]')
    USERNAME_ERROR = (AppiumBy.XPATH, '//android.widget.TextView[@text="Username is required"]')
    PASSWORD_ERROR = (AppiumBy.XPATH, '//android.widget.TextView[@text="Password is required"]')

    # ─── Actions ──────────────────────────────────────────────────────────────
    def enter_username(self, username: str):
        self.type_text(self.USERNAME_FIELD, username)

    def enter_password(self, password: str):
        self.type_text(self.PASSWORD_FIELD, password)

    def tap_login(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, username: str, password: str):
        """Full login: fills in credentials and taps the button."""
        self.enter_username(username)
        self.enter_password(password)
        self.tap_login()

    # ─── Assertion helpers ────────────────────────────────────────────────────
    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)

    def is_username_error_shown(self) -> bool:
        return self.is_visible(self.USERNAME_ERROR)

    def is_password_error_shown(self) -> bool:
        return self.is_visible(self.PASSWORD_ERROR)
