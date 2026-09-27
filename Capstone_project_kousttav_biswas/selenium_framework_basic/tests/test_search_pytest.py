"""
test_search_pytest.py
------------------------
Run with:
    pytest tests/test_search_pytest.py
"""

import os
import csv
import pytest

from pages.home_page import HomePage
from pages.search_page import SearchPage


def read_csv(file_name):
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(project_root, "testdata", file_name)
    with open(path) as f:
        reader = csv.DictReader(f)
        return list(reader)


search_data = read_csv("search_data.csv")


def test_navigate_to_products_page(driver):
    home_page = HomePage(driver)
    home_page.go_to_products_page()
    assert "/products" in driver.current_url


@pytest.mark.parametrize(
    "row",
    search_data,
    ids=[row["test_case"] for row in search_data],
)
def test_product_search_scenarios(driver, row):
    home_page = HomePage(driver)
    search_page = SearchPage(driver)

    home_page.go_to_products_page()
    search_page.search_product(row["search_term"])

    result_count = search_page.get_result_count()

    if row["expect_results"] == "yes":
        assert result_count > 0, "Expected results for " + row["search_term"]
    else:
        assert result_count == 0, "Expected no results for " + row["search_term"]
