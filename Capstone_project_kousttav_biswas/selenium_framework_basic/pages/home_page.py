from selenium.webdriver.common.by import By
import time

from config import BASE_URL


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def go_to_login_page(self):
        # automationexercise.com sometimes shows a full-page Google ad
        # ("google_vignette") right when you click a nav link, which
        # swallows the click and leaves you stuck on that ad instead of
        # the real page. Navigating straight to the URL avoids that
        # click getting intercepted.
        self.driver.get(BASE_URL + "/login")
        time.sleep(2)
        if "google_vignette" in self.driver.current_url:
            # The ad still slipped in on page load - reload once.
            time.sleep(2)
            self.driver.get(BASE_URL + "/login")
            time.sleep(2)

    def go_to_products_page(self):
        self.driver.get(BASE_URL + "/products")
        time.sleep(2)
        if "google_vignette" in self.driver.current_url:
            time.sleep(2)
            self.driver.get(BASE_URL + "/products")
            time.sleep(2)

    def is_logged_in(self):
        # No explicit wait here on purpose (matches course style) -
        # a short sleep before calling this gives the page time to update.
        try:
            self.driver.find_element(By.XPATH, "//a[contains(text(),'Logged in as')]")
            return True
        except Exception:
            return False

    def logout(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Logout')]").click()
        time.sleep(2)
