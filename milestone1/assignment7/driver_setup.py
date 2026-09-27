from selenium import webdriver

class DriverSetup:

    @staticmethod
    def get_driver():
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver