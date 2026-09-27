from behave import given, when, then
from pages.login_page import LoginPage

@given('User launches SauceDemo website')
def step_impl(context):
    context.driver.get("https://www.saucedemo.com/")
    context.login_page = LoginPage(context.driver)

@when('User enters username "{username}"')
def step_impl(context, username):
    context.login_page.enter_username(username)

@when('User enters password "{password}"')
def step_impl(context, password):
    context.login_page.enter_password(password)

@when('User clicks login button')
def step_impl(context):
    context.login_page.click_login()

@then('Verify login result "{result}"')
def step_impl(context, result):

    if result == "success":

        assert "/inventory.html" in context.driver.current_url

    else:

        error_message = context.login_page.get_error_message()

        assert error_message.is_displayed()