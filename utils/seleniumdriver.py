from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pyautogui
import pickle
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium_stealth import stealth

from selenium.webdriver.common.action_chains import ActionChains
def undetectable_driver():
    # Define your headers
    headers = {
        "Host": "i.instagram.com",
        "X-Ig-Connection-Type": "WiFi",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Ig-Capabilities": "36r/Fx8=",
        "User-Agent": "Instagram 159.0.0.28.123 (iPhone8,1; iOS 14_1; en_SA@calendar=gregorian; ar-SA; scale=2.00; 750x1334; 244425769) AppleWebKit/420+",
        "X-Ig-App-Locale": "en",
        "X-Mid": "Ypg64wAAAAGXLOPZjFPNikpr8nJt",
        "Content-Length": "778",
        "Accept-Encoding": "gzip, deflate"
    }
    # mobile_emulation = {
    #     "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
    #     "userAgent": "Mozilla/5.0 (iPad; CPU OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12H143" }

    chrome_options = Options()

    # chrome_options.add_argument('--headless')  # Optional: Run Chrome in headless mode
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument(f"user-agent={headers['User-Agent']}")
    for key, value in headers.items():
        chrome_options.add_argument(f"--{key}={value}")


    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_experimental_option('excludeSwitches',["enable-automation"])
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)
    stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win64",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )
    return driver
