from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()

    # Enter text
    driver.find_element(By.ID, "name").send_keys("Kousttav")

    # Alert Box
    driver.find_element(By.ID, "alertbtn").click()

    alert = driver.switch_to.alert
    print("Alert Text:", alert.text)
    alert.accept()

    # Confirm Box
    driver.find_element(By.ID, "confirmbtn").click()

    confirm = driver.switch_to.alert
    print("Confirm Text:", confirm.text)
    confirm.dismiss()

finally:
    driver.quit()