"""
Desired Capabilities for Android and iOS.

How to configure:
  - Set ANDROID_DEVICE_NAME to your emulator name:
      `adb devices` → copy the name shown
  - Set IOS_DEVICE_NAME to your simulator name:
      `xcrun simctl list devices` → copy the exact name
  - The APK/IPA is downloaded automatically from Sauce Labs public releases.
  - APPIUM_HOST points to localhost:4723 by default (Appium 2.x).
    Change it to Sauce Labs / BrowserStack for cloud execution.
"""

import os
from dotenv import load_dotenv

load_dotenv()

# ─── Appium server ────────────────────────────────────────────────────────────
APPIUM_HOST = os.getenv("APPIUM_HOST", "http://127.0.0.1:4723")

# ─── Local app paths ──────────────────────────────────────────────────────────
# Sauce Labs demo apps are public and free:
# https://github.com/saucelabs/my-demo-app-android
# https://github.com/saucelabs/my-demo-app-ios
ANDROID_APP_PATH = os.path.abspath(
    os.getenv("ANDROID_APP_PATH", "apps/my-demo-app-android.apk")
)
IOS_APP_PATH = os.path.abspath(
    os.getenv("IOS_APP_PATH", "apps/my-demo-app-ios.app.zip")
)

# ─── Android ──────────────────────────────────────────────────────────────────
ANDROID_CAPS = {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:deviceName": os.getenv("ANDROID_DEVICE_NAME", "emulator-5554"),
    "appium:platformVersion": os.getenv("ANDROID_PLATFORM_VERSION", "14.0"),
    "appium:app": ANDROID_APP_PATH,
    "appium:appPackage": "com.saucelabs.mydemoapp.android",
    "appium:appActivity": "com.saucelabs.mydemoapp.android.MainActivity",
    "appium:autoGrantPermissions": True,
    "appium:noReset": False,
    "appium:newCommandTimeout": 120,
}

# ─── iOS ──────────────────────────────────────────────────────────────────────
IOS_CAPS = {
    "platformName": "iOS",
    "appium:automationName": "XCUITest",
    "appium:deviceName": os.getenv("IOS_DEVICE_NAME", "iPhone 15"),
    "appium:platformVersion": os.getenv("IOS_PLATFORM_VERSION", "17.0"),
    "appium:app": IOS_APP_PATH,
    "appium:bundleId": "com.saucelabs.mydemoapp.ios",
    "appium:autoAcceptAlerts": True,
    "appium:noReset": False,
    "appium:newCommandTimeout": 120,
}
