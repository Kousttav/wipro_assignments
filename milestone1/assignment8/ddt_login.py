import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

data = pd.read_csv("testdata.csv")

driver = webdriver.Chrome()

for index, row in data.iterrows():

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").clear()
    driver.find_element(By.ID, "user-name").send_keys(row["username"])

    driver.find_element(By.NAME, "password").clear()
    driver.find_element(By.NAME, "password").send_keys(row["password"])

    driver.find_element(By.XPATH, "//input[@type='submit']").click()

    if row["expected"] == "success":
        assert "/inventory.html" in driver.current_url
        print(f"{row['username']} -> PASS")

    else:
        error_msg = driver.find_element(
            By.XPATH,
            "//h3[@data-test='error']"
        ).text

        assert len(error_msg) > 0
        print(f"{row['username']} -> Error Validated")

driver.quit()