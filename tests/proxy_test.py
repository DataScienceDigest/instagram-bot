from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.common.by import By
import time
chrome_options = Options()
PROXY = "34.162.53.144:8585"
chrome_options.add_argument('--proxy-server=%s' % PROXY)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_experimental_option('excludeSwitches',["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")
# 34.162.53.144	8585


# options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

url = "https://www.instagram.com/"
driver.get(url)
time.sleep(90)

# driver.quit()