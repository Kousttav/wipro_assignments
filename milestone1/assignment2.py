from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
    driver.maximize_window()

    # Click Start button
    driver.find_element(By.XPATH, "//button[text()='Start']").click()

    # Explicit Wait
    wait = WebDriverWait(driver, 10)

    text_element = wait.until(
        EC.visibility_of_element_located((By.ID, "finish"))
    )

    print("Extracted Text:", text_element.text)

finally:
    driver.quit()