from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()

    wait = WebDriverWait(driver, 15)

    # Switch to iframe
    wait.until(
        EC.frame_to_be_available_and_switch_to_it(
            (By.ID, "courses-iframe")
        )
    )

    print("Successfully switched to iframe")

    # Interact with an element inside iframe
    first_link = wait.until(
        EC.presence_of_element_located((By.TAG_NAME, "a"))
    )

    print("Element inside iframe found:")
    print(first_link.text)

    # Back to main page
    driver.switch_to.default_content()

    print("Returned to main page")

    # Open new window
    driver.find_element(By.ID, "openwindow").click()

    parent_window = driver.current_window_handle

    wait.until(lambda d: len(d.window_handles) > 1)

    for handle in driver.window_handles:
        if handle != parent_window:
            driver.switch_to.window(handle)

            print("New Window Title:")
            print(driver.title)

            driver.close()

            break

    driver.switch_to.window(parent_window)

    print("Back to Parent Window")
    print(driver.title)

finally:
    driver.quit()