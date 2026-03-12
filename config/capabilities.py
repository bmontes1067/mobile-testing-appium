"""
Desired Capabilities para Android e iOS.

Cómo usarlas:
  - Ajusta ANDROID_DEVICE_NAME con el nombre de tu emulador:
      `adb devices` → copia el nombre que aparece
  - Ajusta IOS_DEVICE_NAME con el nombre de tu simulador:
      `xcrun simctl list devices` → copia el nombre exacto
  - La APK/IPA se descarga automáticamente desde las URLs públicas
    de Sauce Labs al primer `pytest` si no existe en apps/.
  - APPIUM_HOST apunta a localhost:4723 por defecto (Appium 2.x).
    Cámbialo a Sauce Labs / BrowserStack si usas cloud.
"""

import os
from dotenv import load_dotenv

load_dotenv()

# ─── Servidor Appium ──────────────────────────────────────────────────────────
APPIUM_HOST = os.getenv("APPIUM_HOST", "http://127.0.0.1:4723")

# ─── Rutas locales de la app ──────────────────────────────────────────────────
# Las apps de demo de Sauce Labs son públicas y gratuitas:
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
