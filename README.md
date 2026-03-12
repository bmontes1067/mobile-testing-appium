# 📱 Mobile Testing — Appium + Python

![CI](https://github.com/bmontes1067/mobile-testing-appium/actions/workflows/mobile-tests.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![Appium](https://img.shields.io/badge/Appium-2.x-662D91?logo=appium&logoColor=white)
![Platforms](https://img.shields.io/badge/Platforms-Android%20%7C%20iOS-success)
![License](https://img.shields.io/badge/License-MIT-yellow)

Mobile automation framework built with **Appium 2**, **Python** and **pytest**.
Covers Android and iOS using the [Sauce Labs My Demo App](https://github.com/saucelabs/my-demo-app-android) as the test target.
**Page Object Model** architecture with reusable fixtures and automatic screenshots on failure.

---

## 🏗 Structure

```
mobile-testing-appium/
├── config/
│   └── capabilities.py         # Desired capabilities for Android + iOS
├── pages/
│   ├── android/                # Android Page Objects (UiAutomator2)
│   │   ├── base_page.py
│   │   ├── login_page.py
│   │   ├── catalog_page.py
│   │   ├── cart_page.py
│   │   └── checkout_page.py
│   └── ios/                    # iOS Page Objects (XCUITest)
│       ├── base_page.py
│       ├── login_page.py
│       ├── catalog_page.py
│       ├── cart_page.py
│       └── checkout_page.py
├── tests/
│   ├── android/                # 17 Android tests
│   ├── ios/                    # 8 iOS tests
│   └── common/                 # 4 cross-platform tests
├── utils/
│   ├── driver_factory.py       # Creates the driver based on platform
│   └── helpers.py              # scroll, screenshot, wait helpers
├── scripts/
│   └── download_apps.py        # Downloads APK/IPA from Sauce Labs
├── conftest.py
├── pytest.ini
└── requirements.txt
```

---

## 🛠 Stack

| Tool | Version | Role |
|------|---------|------|
| Appium | 2.x | Mobile automation server |
| Appium Python Client | 3.1.x | Python SDK |
| UiAutomator2 | — | Android driver |
| XCUITest | — | iOS driver (Mac only) |
| pytest | 8.x | Test framework |
| pytest-html | 4.x | HTML reports |

---

## 🚀 Getting started

### 1. Prerequisites

**Android:**
- Android Studio with an emulator created
- Environment variables configured:
```bash
export ANDROID_HOME=$HOME/Library/Android/sdk
export PATH=$PATH:$ANDROID_HOME/platform-tools
```

**iOS (Mac only):**
- Xcode with simulators installed

### 2. Install Appium 2

```bash
npm install -g appium
appium driver install uiautomator2   # Android
appium driver install xcuitest       # iOS (Mac only)
```

### 3. Install Python dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Download the demo app

```bash
python scripts/download_apps.py --platform android
python scripts/download_apps.py --platform ios
```

### 5. Configure your emulator/simulator

Copy `.env.example` to `.env` and fill in your values:

```bash
cp .env.example .env
```

```bash
# Android: get your emulator name
adb devices
# → emulator-5554

# iOS: get your simulator name
xcrun simctl list devices | grep "iPhone"
# → iPhone 15
```

### 6. Start Appium

```bash
appium
# Appium REST http interface listener started on 0.0.0.0:4723
```

### 7. Run the tests

```bash
# Android
pytest tests/android/ --platform android -v

# iOS
pytest tests/ios/ --platform ios -v

# Single test
pytest tests/android/test_login.py::TestLoginAndroid::test_login_valid_credentials -v
```

The HTML report is generated at `reports/report.html`.

---

## 📊 Test coverage

| Suite | Platform | Tests |
|-------|----------|-------|
| test_login | Android | 7 |
| test_catalog | Android | 6 |
| test_checkout | Android | 4 |
| test_login | iOS | 4 |
| test_catalog | iOS | 4 |
| test_cross_platform | Android + iOS | 4 |
| **Total** | | **29** |

---

## 🤖 CI/CD

- **Every push/PR:** lint + collect (ubuntu-latest, no device needed)
- **Merge to main:** Android tests on emulator (ubuntu-latest + KVM) + iOS tests on simulator (macos-latest)
- HTML reports uploaded as GitHub Actions artifacts

---

## 📄 License

MIT © [Belén Montes](https://github.com/bmontes1067)
