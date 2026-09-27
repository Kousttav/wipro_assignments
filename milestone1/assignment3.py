from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    # Checkboxes
    checkbox1 = driver.find_element(By.ID, "checkBoxOption1")
    checkbox3 = driver.find_element(By.ID, "checkBoxOption3")

    checkbox1.click()
    checkbox3.click()

    print("Checkbox 1 Selected:", checkbox1.is_selected())
    print("Checkbox 3 Selected:", checkbox3.is_selected())

    # Autocomplete Dropdown
    dropdown = driver.find_element(By.ID, "autocomplete")
    dropdown.send_keys("Ind")

    suggestions = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "li.ui-menu-item div")
        )
    )

    for option in suggestions:
        if option.text == "India":
            option.click()
            print("Selected:", option.text)
            break

finally:
    driver.quit()