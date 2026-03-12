"""
Reusable helpers for mobile tests:
  - scroll (Android UiScrollable + iOS swipe)
  - screenshot with automatic naming
  - wait_for_element with retry
"""

import os
from datetime import datetime
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


SCREENSHOT_DIR = "reports/screenshots"


def take_screenshot(driver, name: str = "") -> str:
    """Saves a screenshot to reports/screenshots/ and returns the path."""
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{SCREENSHOT_DIR}/{name}_{ts}.png" if name else f"{SCREENSHOT_DIR}/{ts}.png"
    driver.save_screenshot(filename)
    return filename


def wait_for_element(driver, locator: tuple, timeout: int = 10):
    """
    Waits for an element to be visible and returns it.

    Args:
        driver: Appium driver instance
        locator: tuple (AppiumBy.X, "value")
        timeout: maximum seconds to wait

    Returns:
        WebElement
    Raises:
        TimeoutException if the element does not appear within timeout seconds.
    """
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )


def wait_and_click(driver, locator: tuple, timeout: int = 10):
    """Waits for an element to be clickable and clicks it."""
    el = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )
    el.click()
    return el


def scroll_down_android(driver, swipes: int = 1):
    """Scrolls down on Android using UiScrollable."""
    for _ in range(swipes):
        driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true)).scrollForward()'
        )


def scroll_up_android(driver, swipes: int = 1):
    """Scrolls up on Android using UiScrollable."""
    for _ in range(swipes):
        driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true)).scrollBackward()'
        )


def swipe_ios(driver, direction: str = "up"):
    """
    Swipes on iOS using the mobile: scroll command.
    direction: "up" | "down" | "left" | "right"
    """
    driver.execute_script("mobile: scroll", {"direction": direction})


def get_platform(driver) -> str:
    """Returns 'android' or 'ios' based on the active driver."""
    caps = driver.capabilities
    return caps.get("platformName", "").lower()
