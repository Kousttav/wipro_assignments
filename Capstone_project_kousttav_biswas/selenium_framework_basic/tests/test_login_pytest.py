"""
test_login_pytest.py
----------------------
Run with:
    pytest tests/test_login_pytest.py
"""

import os
import csv
import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage


def read_csv(file_name):
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(project_root, "testdata", file_name)
    with open(path) as f:
        reader = csv.DictReader(f)
        return list(reader)


login_data = read_csv("login_data.csv")


def test_navigate_to_login_page(driver):
    home_page = HomePage(driver)
    home_page.go_to_login_page()
    assert "/login" in driver.current_url


@pytest.mark.parametrize(
    "row",
    login_data,
    ids=[row["test_case"] for row in login_data],
)
def test_login_scenarios(driver, row):
    # NOTE: put a real registered automationexercise.com account in
    # the 'valid_login' row of testdata/login_data.csv before running.
    home_page = HomePage(driver)
    login_page = LoginPage(driver)

    home_page.go_to_login_page()
    login_page.login(row["email"], row["password"])

    if row["expected_result"] == "success":
        assert home_page.is_logged_in(), "Expected login to succeed for " + row["test_case"]
        home_page.logout()
    else:
        assert not home_page.is_logged_in(), "Expected login to fail for " + row["test_case"]
