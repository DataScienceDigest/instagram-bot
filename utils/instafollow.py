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

mobile_emulation = {
    "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }

chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_experimental_option('excludeSwitches',["enable-automation"])
# chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(
    executable_path=r"C:\Users\hp\Documents\insta_create\hikke\chromedriver.exe", chrome_options=chrome_options
)
stealth(driver,
      languages=["en-US", "en"],
      vendor="Google Inc.",
      platform="Win64",
      webgl_vendor="Intel Inc.",
      renderer="Intel Iris OpenGL Engine",
      fix_hairline=True,
  )
url = "https://www.instagram.com/login"
driver.get(url)

username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME,"username")))
password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME,"password")))
username_input.send_keys("anamdnowm2992")
password_input.send_keys("shiv1915")
login_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,"//button[@type='submit']")))

login_button.click()
print("loged in")
#___________follow suggested _______________________________

WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,'//div[@class="x9f619 xxk0z11 xvy4d1p x11xpdln xii2z7h x19c4wfv"]/*[name()="svg"][@aria-label="Home"]'))).click()
print("home button clicked")
sleep(10)
driver.find_element(By.XPATH,"//button[normalize-space()='Not Now']").click()
print("not now clicked")
# _________ this function works when the account already follow some other accounts 
def follow_suggested():
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,"//div[@class='_aacl _aacn _aacw _aacx _aad6']"))).click()
    print('follow suggested clicked')
# follow_suggested()
# __________________________________________
print(" ___________ working good ______________________")

# def follow_all():
print("follow all click")
# for i in range(10):
#     sleep(5)
buttons = WebDriverWait(driver,30).until(EC.presence_of_all_elements_located((By.XPATH,"//button[contains(.,'Follow')]")))
# //div[@id='f3b3f1978f4ab3c']//div[contains(@class,'_aacl _aaco _aacw _aad6 _aade')][normalize-space()='Follow']
# buttons = driver.find_elements(By.XPATH,"//button[contains(.,'Follow')]")
sleep(15)
print(len(buttons))
for btn in buttons:
    print(btn)
    sleep(2)
    btn.click()
print("______________completed__________________________")
# Use the Java script to click on follow because after the scroll down the buttons will be un clickeable unless you go to it's location
    # driver.execute_script("arguments[0].click();", btn)
    # sleep(3)
# follow_all()