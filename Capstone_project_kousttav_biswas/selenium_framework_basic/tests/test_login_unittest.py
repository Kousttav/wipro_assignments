"""
test_login_unittest.py
------------------------
Run with:
    python -m unittest tests.test_login_unittest -v
"""

import os
import sys
import csv
import unittest

# Let this file find config.py and pages/ which sit one folder up
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import get_driver, BASE_URL
from pages.home_page import HomePage
from pages.login_page import LoginPage


def read_csv(file_name):
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(project_root, "testdata", file_name)
    with open(path) as f:
        reader = csv.DictReader(f)
        return list(reader)


class TestLoginUnittest(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()
        self.driver.get(BASE_URL)
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        # If the test failed or errored, save a screenshot before closing.
        # NOTE: when this file runs under plain "python -m unittest", the
        # result object has .failures/.errors lists. When pytest runs the
        # SAME file (it auto-discovers unittest classes too), pytest wraps
        # things differently and those attributes don't exist - so we use
        # getattr(..., []) instead of assuming they're always there.
        outcome = getattr(self, "_outcome", None)
        failed = False
        if outcome is not None:
            result = getattr(outcome, "result", None)
            if result is not None:
                failures = getattr(result, "failures", [])
                errors = getattr(result, "errors", [])
                failed = any(test is self for test, _ in failures) or any(
                    test is self for test, _ in errors
                )
        if failed:
            project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            screenshot_dir = os.path.join(project_root, "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            self.driver.save_screenshot(
                os.path.join(screenshot_dir, self._testMethodName + ".png")
            )
        self.driver.quit()

    def test_navigate_to_login_page(self):
        self.home_page.go_to_login_page()
        self.assertIn("/login", self.driver.current_url)

    def test_login_scenarios_from_csv(self):
        # NOTE: put a real registered automationexercise.com account in
        # the 'valid_login' row of testdata/login_data.csv before running.
        data = read_csv("login_data.csv")
        for row in data:
            with self.subTest(case=row["test_case"]):
                self.driver.get(BASE_URL)
                self.home_page.go_to_login_page()
                self.login_page.login(row["email"], row["password"])

                if row["expected_result"] == "success":
                    self.assertTrue(
                        self.home_page.is_logged_in(),
                        "Expected login to succeed for " + row["test_case"],
                    )
                    self.home_page.logout()
                else:
                    self.assertFalse(
                        self.home_page.is_logged_in(),
                        "Expected login to fail for " + row["test_case"],
                    )


if __name__ == "__main__":
    unittest.main()
