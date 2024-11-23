# username search --> like the posts hyoot8899 shiv1915 mojjo5667

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pyautogui
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
from selenium.webdriver.common.action_chains import ActionChains
from essential_generators import DocumentGenerator
gen = DocumentGenerator()
chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_experimental_option('excludeSwitches',["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome( options=chrome_options)
stealth(driver,
      languages=["en-US", "en"],
      vendor="Google Inc.",
      platform="Win64",
      webgl_vendor="Intel Inc.",
      renderer="Intel Iris OpenGL Engine",
      fix_hairline=True,
  )
url = "https://www.instagram.com"
driver.get(url)
username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME,"username")))
password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME,"password")))
username_input.send_keys("himanikull")
password_input.send_keys("shiv1915")
login_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,"//button[@type='submit']")))

login_button.click()
print("loged in")
sleep(5)
url = "https://www.instagram.com/himanikull"
driver.get(url)
sleep(5)

WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"//a[normalize-space()='Edit profile']"))).click()
print("edit profile clicked")
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Change photo')]"))
)
element.click()
print("change profile clicked")
pathname = r"C:\Users\hp\Documents\insta_create\hikke\imagesss\Shayari-Wallpaper-42-1.jpg"
print(pathname)
sleep(5)
pyautogui.typewrite(pathname)
print("pyautogui working")
sleep(5)
pyautogui.press("enter")
s = gen.sentence()
print(s)
driver.find_element(By.XPATH,"//textarea[@id='pepBio']").send_keys(s)
print("bio added")
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Submit')]"))
)
element.click()
print('bio updated')
# def update_profile():
#     print('profile updater working')