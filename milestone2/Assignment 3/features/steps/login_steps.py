from behave import given, when, then

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@given('User launches SauceDemo website')
def step_impl(context):
    context.driver.get("https://www.saucedemo.com/")
    context.login_page = LoginPage(context.driver)

@when('User logs in with username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.login_page.login(username, password)

@then('User should be redirected to inventory page')
def step_impl(context):
    inventory_page = InventoryPage(context.driver)

    assert "/inventory.html" in inventory_page.get_current_url()