from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()

    rows = driver.find_elements(
        By.XPATH,
        "//table[@id='product']/tbody/tr"
    )

    target_course = "Learn SQL in Practical + Database Testing from Scratch"

    course_found = False

    for row in rows[1:]:
        cols = row.find_elements(By.TAG_NAME, "td")

        if len(cols) > 0 and cols[1].text == target_course:

            instructor = cols[0].text
            price = cols[2].text

            course_found = True

            assert instructor != ""
            assert price != ""

            break

    assert course_found

finally:
    driver.quit()