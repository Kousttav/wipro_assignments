import os
import sys

# Add assignment7 folder to Python path
sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from driver_setup import DriverSetup
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

driver = DriverSetup.get_driver()

try:
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    assert "/inventory.html" in inventory_page.get_current_url()

    print("Login Test Passed")

finally:
    driver.quit()