# 📱 Mobile Testing — Appium + Python

![CI](https://github.com/bmontes1067/mobile-testing-appium/actions/workflows/mobile-tests.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![Appium](https://img.shields.io/badge/Appium-2.x-662D91?logo=appium&logoColor=white)
![Platforms](https://img.shields.io/badge/Platforms-Android%20%7C%20iOS-success)
![License](https://img.shields.io/badge/License-MIT-yellow)

Framework de automatización móvil con **Appium 2**, **Python** y **pytest**.
Cubre Android e iOS usando la [Sauce Labs My Demo App](https://github.com/saucelabs/my-demo-app-android) como target.
Arquitectura **Page Object Model** con fixtures reutilizables y screenshots automáticos en fallos.

---

## 🏗 Estructura

```
mobile-testing-appium/
├── config/
│   └── capabilities.py         # Desired capabilities Android + iOS
├── pages/
│   ├── android/                # Page Objects Android (UiAutomator2)
│   │   ├── base_page.py
│   │   ├── login_page.py
│   │   ├── catalog_page.py
│   │   ├── cart_page.py
│   │   └── checkout_page.py
│   └── ios/                    # Page Objects iOS (XCUITest)
│       ├── base_page.py
│       ├── login_page.py
│       ├── catalog_page.py
│       ├── cart_page.py
│       └── checkout_page.py
├── tests/
│   ├── android/                # 17 tests Android
│   ├── ios/                    # 8 tests iOS
│   └── common/                 # 4 tests cross-platform
├── utils/
│   ├── driver_factory.py       # Crea el driver según plataforma
│   └── helpers.py              # scroll, screenshot, wait
├── scripts/
│   └── download_apps.py        # Descarga APK/IPA de Sauce Labs
├── conftest.py
├── pytest.ini
└── requirements.txt
```

---

## 🛠 Stack

| Herramienta | Versión | Rol |
|-------------|---------|-----|
| Appium | 2.x | Servidor de automatización móvil |
| Appium Python Client | 3.1.x | SDK Python |
| UiAutomator2 | — | Driver Android |
| XCUITest | — | Driver iOS (solo Mac) |
| pytest | 8.x | Framework de tests |
| pytest-html | 4.x | Reportes HTML |

---

## 🚀 Cómo ejecutar

### 1. Requisitos previos

**Android:**
- Android Studio con un emulador creado
- Variables de entorno configuradas:
```bash
export ANDROID_HOME=$HOME/Library/Android/sdk
export PATH=$PATH:$ANDROID_HOME/platform-tools
```

**iOS (solo Mac):**
- Xcode con simuladores instalados

### 2. Instalar Appium 2

```bash
npm install -g appium
appium driver install uiautomator2   # Android
appium driver install xcuitest       # iOS (solo Mac)
```

### 3. Instalar dependencias Python

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Descargar la app de demo

```bash
python scripts/download_apps.py --platform android
python scripts/download_apps.py --platform ios
```

### 5. Configurar el emulador/simulador

Edita `.env` con tus valores:

```bash
# Android: nombre de tu emulador
adb devices
# → emulator-5554

# iOS: nombre de tu simulador
xcrun simctl list devices | grep "iPhone"
# → iPhone 15
```

### 6. Arrancar Appium

```bash
appium
# Appium REST http interface listener started on 0.0.0.0:4723
```

### 7. Ejecutar tests

```bash
# Android
pytest tests/android/ --platform android -v

# iOS
pytest tests/ios/ --platform ios -v

# Solo un test
pytest tests/android/test_login.py::TestLoginAndroid::test_login_valid_credentials -v
```

El reporte HTML se genera en `reports/report.html`.

---

## 📊 Cobertura

| Suite | Plataforma | Tests |
|-------|-----------|-------|
| test_login | Android | 7 |
| test_catalog | Android | 6 |
| test_checkout | Android | 4 |
| test_login | iOS | 4 |
| test_catalog | iOS | 4 |
| test_cross_platform | Android + iOS | 4 |
| **Total** | | **29** |

---

## 🤖 CI/CD

- **Cada push/PR:** lint + collect (ubuntu-latest, sin dispositivo)
- **Merge a main:** tests Android en emulador (ubuntu-latest + KVM) + tests iOS en simulador (macos-latest)
- Los reportes HTML se suben como artefactos de GitHub Actions

---

## 📄 License

MIT © [Belén Montes](https://github.com/bmontes1067)
