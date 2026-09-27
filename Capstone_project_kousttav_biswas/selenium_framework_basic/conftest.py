"""
conftest.py
------------
Simple fixture that opens the browser before each test and closes it
after. If a test fails, a screenshot is saved automatically.
"""

import os
import pytest

from config import get_driver, BASE_URL


@pytest.fixture
def driver():
    drv = get_driver()
    drv.get(BASE_URL)
    yield drv
    drv.quit()


def pytest_runtest_makereport(item, call):
    if call.when == "call" and call.excinfo is not None:
        drv = item.funcargs.get("driver")
        if drv is not None:
            project_root = os.path.dirname(os.path.abspath(__file__))
            screenshot_dir = os.path.join(project_root, "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            drv.save_screenshot(os.path.join(screenshot_dir, item.name + ".png"))
