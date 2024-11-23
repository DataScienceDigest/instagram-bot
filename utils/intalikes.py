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
username_input.send_keys("gynnnn2023")
password_input.send_keys("shiv1915")
login_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,"//button[@type='submit']")))

login_button.click()
print("loged in ")
# sleep(25)
def search():
    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CSS_SELECTOR,"[aria-label='Search']"))).click()
    print('search clicked')
    username = 'ovsvffrqik'
    driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys(username)
    
    print(username)
    
    sleep(5)
    WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,f"//*[contains(text(),'ovsvffrqik')]"))).click()
    sleep(5)
    print('username found successful')

    sleep(5)
    ################### for follow the accoutn ##############################
    
    ##########################################################################
    WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CLASS_NAME,"_aagw"))).click()
    # --------------------this is next post------------------
    s = driver.find_element(By.CSS_SELECTOR,"span[class='_ac2a']")
    t = s.text
    no_of_posts = int(t)
    print(no_of_posts)
    for i in range(no_of_posts):
        print(i+1,"----------")
        try:
            driver.find_element(By.XPATH,"//button/div/*[*[local-name()='svg']/@aria-label='Unlike']/*")
            print("Already liked this post")
            try:
                next_post = driver.find_element(By.CSS_SELECTOR,"div._aaqg._aaqh")
                ele = next_post.find_element(By.CSS_SELECTOR,"button._abl-")
                ele.click()
            except:
                print('no more posts available')
            print('next post clicked')
        except Exception:
            # Like
            driver.find_element(By.XPATH,"//button/div/*[*[local-name()='svg']/@aria-label='Like']/*").click()
            print("Liked")
            try:
                next_post = driver.find_element(By.CSS_SELECTOR,"div._aaqg._aaqh")
                ele = next_post.find_element(By.CSS_SELECTOR,"button._abl-")
                ele.click()
            except:
                print('no more posts available')
            print('next post clicked')
       
#__________________________________________________________
search()
# __________ completed__________________________________-_______--