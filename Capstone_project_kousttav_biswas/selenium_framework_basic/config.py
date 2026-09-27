from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# Change these two values to control the whole run
BROWSER = "chrome"          # "chrome" or "firefox"
BASE_URL = "https://automationexercise.com"


def get_driver():
    if BROWSER.lower() == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif BROWSER.lower() == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise Exception("Invalid browser name. Please choose 'chrome' or 'firefox'.")

    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver
