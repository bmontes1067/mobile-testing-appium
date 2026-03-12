"""
DriverFactory: crea y devuelve un driver Appium según la plataforma.

Uso típico (en conftest.py):
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
            Instancia de webdriver.Remote lista para usar.
        Raises:
            ValueError: si la plataforma no es válida.
        """
        platform = platform.lower()

        if platform == "android":
            caps = ANDROID_CAPS
        elif platform == "ios":
            caps = IOS_CAPS
        else:
            raise ValueError(f"Plataforma no soportada: '{platform}'. Usa 'android' o 'ios'.")

        options = AppiumOptions()
        for key, value in caps.items():
            options.set_capability(key, value)

        driver = webdriver.Remote(
            command_executor=APPIUM_HOST,
            options=options,
        )
        driver.implicitly_wait(10)
        return driver
