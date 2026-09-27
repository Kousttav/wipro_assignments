from selenium.webdriver.common.by import By
import time


class SearchPage:

    def __init__(self, driver):
        self.driver = driver

    def search_product(self, keyword):
        self.driver.find_element(By.ID, "search_product").send_keys(keyword)
        time.sleep(1)
        self.driver.find_element(By.ID, "submit_search").click()
        time.sleep(2)

    def get_result_count(self):
        products = self.driver.find_elements(By.CSS_SELECTOR, ".product-image-wrapper")
        return len(products)
