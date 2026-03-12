"""
conftest.py — Appium fixtures for Android and iOS.

How to select the platform:
    pytest tests/android/          # Android only
    pytest tests/ios/              # iOS only
    pytest --platform android      # explicit flag
    pytest --platform ios

The `driver` fixture starts Appium, runs the test, and closes the session.
If a test fails, a screenshot is saved automatically to reports/screenshots/.
"""

import pytest
from utils.driver_factory import DriverFactory
from utils.helpers import take_screenshot


def pytest_addoption(parser):
    parser.addoption(
        "--platform",
        action="store",
        default="android",
        help="Target platform: android | ios",
    )


@pytest.fixture(scope="function")
def driver(request):
    """
    Main fixture: creates the driver for the given platform,
    injects it into the test, and quits after the test completes.
    Takes an automatic screenshot on failure.
    """
    marker = request.node.get_closest_marker("platform")
    if marker:
        platform = marker.args[0]
    else:
        platform = request.config.getoption("--platform", default="android")

    d = DriverFactory.create(platform)
    yield d

    if request.node.rep_call.failed if hasattr(request.node, "rep_call") else False:
        take_screenshot(d, f"FAILED_{request.node.name}")

    d.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to expose the test result to the driver fixture."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
