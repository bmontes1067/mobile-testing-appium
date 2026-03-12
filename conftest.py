"""
conftest.py — fixtures de Appium para Android e iOS.

Cómo seleccionar plataforma al ejecutar:
    pytest tests/android/          # sólo Android
    pytest tests/ios/              # sólo iOS
    pytest --platform android      # flag explícito
    pytest --platform ios

El fixture `driver` arranca Appium, ejecuta el test y cierra la sesión.
Si el test falla, se guarda un screenshot automáticamente en reports/screenshots/.
"""

import pytest
from utils.driver_factory import DriverFactory
from utils.helpers import take_screenshot


def pytest_addoption(parser):
    parser.addoption(
        "--platform",
        action="store",
        default="android",
        help="Plataforma objetivo: android | ios",
    )


@pytest.fixture(scope="function")
def driver(request):
    """
    Fixture principal: crea el driver según la plataforma,
    lo inyecta en el test y lo cierra al finalizar.
    Hace screenshot automático en caso de fallo.
    """
    # La plataforma puede venir del flag --platform o del marker @pytest.mark.platform
    marker = request.node.get_closest_marker("platform")
    if marker:
        platform = marker.args[0]
    else:
        platform = request.config.getoption("--platform", default="android")

    d = DriverFactory.create(platform)
    yield d

    # Teardown: screenshot si el test falló
    if request.node.rep_call.failed if hasattr(request.node, "rep_call") else False:
        take_screenshot(d, f"FAILED_{request.node.name}")

    d.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook para exponer el resultado del test al fixture driver."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
