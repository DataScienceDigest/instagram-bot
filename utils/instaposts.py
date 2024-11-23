
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pyautogui
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
from pathlib import Path
# mobile_emulation = { 
#     "deviceName": "iPhone 6"
# }
chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_experimental_option('excludeSwitches',["enable-automation"])
# chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(
    executable_path=r"C:\Users\hp\Documents\insta_create\hikke\chromedriver.exe", options=chrome_options
)

directory = "imagesss"
folder_path = r'C:\Users\hp\Documents\insta_create\hikke'
stealth(driver,
      languages=["en-US", "en"],
      vendor="Google Inc.",
      platform="Win64",
      webgl_vendor="Intel Inc.",
      renderer="Intel Iris OpenGL Engine",
      fix_hairline=True,
  )
def insta_login(username,password):
    url = "https://www.instagram.com/"
    driver.get(url)
    username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME,"username")))
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME,"password")))
    username_input.send_keys(username)
    password_input.send_keys(password)
    login_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,"//button[@type='submit']"))).click()
    print("loged in ")

#_________read all posts ____________

def all_pics():
    ls = []
    files = Path(directory).glob('*')
    for file in files:
        ls.append(file)
    return ls
pic_data = all_pics()
print(pic_data,"-------pic data----------")

def not_save():
    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"//button[normalize-space()='Not Now']"))).click()
    print("not save clicked")
    ########________this function will use in try except block_____________
    # go_back = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,"//*[contains(text(), 'Go back to Instagram.')]")))
    # # go_back = driver.find_element(By.XPATH,"//*[contains(text(), 'Go back to Instagram.')]").click()
    # go_back.click()
    #__________ tille here try except block _____________________
    try:
        print('inside try block')
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,"//button[normalize-space()='Not Now']"))).click()
    except:
        print('Inside except block')
    add_button()

def add_button(z):
    # url = "https://www.instagram.com/"
    # driver.get(url)
    print("seach functiom")
    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CSS_SELECTOR,"[aria-label='New post']"))).click()
    print('add search button clicked')
    WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,"//*[contains(text(), 'Select from computer')]"))).click()
    print('upload image clicked')
    pathname = z
    print(pathname)
    print(type(pathname))
    sleep(5)
    pyautogui.typewrite(z)
    print("pyautogui working")
    sleep(10)
    pyautogui.press("enter")
    print('open pressed')
    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"//button[normalize-space()='Next']"))).click()
    print("next button clicked")
    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"//button[normalize-space()='Next']"))).click()
    print("next button2 clicked")
    sleep(5)
    WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,"//button[normalize-space()='Share']"))).click()
    print("next button3 clicked")
    sleep(10)
    # WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,"//h2[@class='_aacl _aacr _aact _aacx _aad6 _aadb']")))
    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'//div[@class="x78zum5 x6s0dn4 xl56j7k xdt5ytf"]/*[name()="svg"][@aria-label="Close"]'))).click()
    print("close button clicked")
insta_login("sk3354580","%S1h9i1v5%")
for i in pic_data:
    z = str(folder_path)+"\\"+str(i)
    print(z)
    add_button(z)
 





















