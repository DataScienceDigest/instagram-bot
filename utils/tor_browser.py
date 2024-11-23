from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from time import sleep 
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from mailtm import Email
from fake_useragent import UserAgent
ua = UserAgent()
import re
import random
# Set up the Tor Browser profile
mobile_emulation = {
        "userAgent": f"{ua.chrome}" 
        }
tor_profile = FirefoxProfile()
service = Service(executable_path=r'C:\Users\hp\Documents\insta_create\hikke\geckodriver.exe')
options = Options()

def tor_driver():
    tor_profile.set_preference('general.useragent.override', f'{mobile_emulation}')
    tor_profile.set_preference('network.proxy.type', 1)
    tor_profile.set_preference('network.proxy.socks', '127.0.0.1')
    tor_profile.set_preference('network.proxy.socks_port', 9150)
    options.profile = tor_profile
    options.set_preference('detach', True)
    driver = webdriver.Firefox(options=options,service=service)
    return driver

