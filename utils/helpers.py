"""
Helpers reutilizables para tests móviles:
  - scroll (Android UiScrollable + iOS swipe)
  - screenshot con nombre automático
  - wait_for_element con retry
"""

import os
import time
from datetime import datetime
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


SCREENSHOT_DIR = "reports/screenshots"


def take_screenshot(driver, name: str = "") -> str:
    """Guarda un screenshot en reports/screenshots/ y devuelve la ruta."""
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{SCREENSHOT_DIR}/{name}_{ts}.png" if name else f"{SCREENSHOT_DIR}/{ts}.png"
    driver.save_screenshot(filename)
    return filename


def wait_for_element(driver, locator: tuple, timeout: int = 10):
    """
    Espera a que un elemento sea visible y lo devuelve.

    Args:
        driver: instancia Appium
        locator: tupla (AppiumBy.X, "valor")
        timeout: segundos máximos de espera

    Returns:
        WebElement
    Raises:
        TimeoutException si el elemento no aparece en timeout segundos.
    """
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )


def wait_and_click(driver, locator: tuple, timeout: int = 10):
    """Espera a que un elemento sea clickable y hace click."""
    el = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )
    el.click()
    return el


def scroll_down_android(driver, swipes: int = 1):
    """Scroll hacia abajo en Android usando UiScrollable."""
    for _ in range(swipes):
        driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true)).scrollForward()'
        )


def scroll_up_android(driver, swipes: int = 1):
    """Scroll hacia arriba en Android."""
    for _ in range(swipes):
        driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true)).scrollBackward()'
        )


def swipe_ios(driver, direction: str = "up"):
    """
    Swipe en iOS usando el comando mobile: scroll.
    direction: "up" | "down" | "left" | "right"
    """
    driver.execute_script("mobile: scroll", {"direction": direction})


def get_platform(driver) -> str:
    """Devuelve 'android' o 'ios' según el driver activo."""
    caps = driver.capabilities
    platform = caps.get("platformName", "").lower()
    return platform
