"""
DriverFactory: creates and returns an Appium driver based on the platform.

Usage (in conftest.py):
    driver = DriverFactory.create("android")
    driver = DriverFactory.create("ios")
"""

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from config.capabilities import APPIUM_HOST, ANDROID_CAPS, IOS_CAPS


class DriverFactory:

    @staticmethod
    def create(platform: str) -> webdriver.Remote:
        """
        Args:
            platform: "android" | "ios"
        Returns:
            A webdriver.Remote instance ready to use.
        Raises:
            ValueError: if the platform is not supported.
        """
        platform = platform.lower()

        if platform == "android":
            options = UiAutomator2Options().load_capabilities(ANDROID_CAPS)
        elif platform == "ios":
            options = XCUITestOptions().load_capabilities(IOS_CAPS)
        else:
            raise ValueError(f"Unsupported platform: '{platform}'. Use 'android' or 'ios'.")

        driver = webdriver.Remote(command_executor=APPIUM_HOST, options=options)
        driver.implicitly_wait(10)
        return driver
