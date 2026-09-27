from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    # Username field using ID
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")

    # Password field using NAME
    password = driver.find_element(By.NAME, "password")
    password.send_keys("secret_sauce")

    # Login button using XPATH
    login_btn = driver.find_element(By.XPATH, "//input[@type='submit']")
    login_btn.click()

    # Validation
    current_url = driver.current_url
    assert "/inventory.html" in current_url

    print("Login Successful")
    print("Current URL:", current_url)

finally:
    driver.quit()