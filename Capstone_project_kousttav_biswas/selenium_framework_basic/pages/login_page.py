from selenium.webdriver.common.by import By
import time


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):
        self.driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-email']").send_keys(email)
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-password']").send_keys(password)
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "button[data-qa='login-button']").click()
        time.sleep(2)

    def get_error_message(self):
        try:
            return self.driver.find_element(By.XPATH, "//p[contains(text(),'incorrect')]").text
        except Exception:
            return ""
