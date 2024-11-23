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
from selenium.webdriver.support.ui import Select
ua = UserAgent()
import re
import random
# Set up the Tor Browser profile
useraget = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
tor_profile = FirefoxProfile()
tor_profile.set_preference('general.useragent.override', f'{useraget}')
tor_profile.set_preference('network.proxy.type', 1)
tor_profile.set_preference('network.proxy.socks', '127.0.0.1')
tor_profile.set_preference('network.proxy.socks_port', 9150)
service = Service(executable_path=r'..\drivers\geckodriver.exe')
options = Options()
 # Set height of the browser window
options.profile = tor_profile
options.set_preference('detach', True)
driver = webdriver.Firefox(options=options,service=service)

driver.get("https://www.instagram.com/accounts/signup/email/")

# time.sleep(40)
# driver.quit()
# jeyesil128  gwkiiii username


try:
    sleep(random.randint(8,10))
    cookie = driver.find_element(By.XPATH,'//button[contains(text(), "Decline optional cookies")]').click()
    sleep(10)
except:
    pass
test = Email()
code = None
listening = True  # Add a flag to control the listener
test.register()
print("\nEmail Address: " + str(test.address))
def listener(message):
    global code
    global listening
    print("\nSubject: " + message['subject'])
    code = message['subject']
    match = re.search(r'\d{6}', code)
    if match:
            code = match.group()
            print(code,'-----------------------')
            print("Confirmation Code is: "+ code)


mail_address = str(test.address)
test.start(listener)

print(mail_address,'-=-=-=-=-=-=')
email_field = driver.find_element(By.NAME,"email")
email_field.send_keys(mail_address)
print('email: ' + mail_address)
print('fill email working-------------------')
#  write code to fill confirmation code here 

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,'//button[contains(text(), "Next")]'))).click()
print('next button clicked')
sleep(8)
driver.find_element(By.NAME,'emailConfirmationCode').send_keys(code)
sleep(random.randint(1,5))
driver.find_element(By.XPATH,"//button[normalize-space()='Next']").click()
#  code to write full name and password 

fullname_field = driver.find_element(By.NAME,"fullName")
fullname_field.send_keys('helowshiv1232')
password_field = driver.find_element(By.NAME,"password")
password_field.send_keys('shiv1915')
driver.find_element(By.XPATH,'//button[contains(text(), "Next")]')
#  code for date of birth -------
test_list = ['January','February','March','April','May','June','July','August','September','October','November','December']
month = random.choice(test_list)
date = random.randint(1,30)
year = random.randint(1990,2004)
print(date,month,year)
birthday_input = Select(driver.find_element(By.CSS_SELECTOR,"select[title='Month:']"))
birthday_input.select_by_visible_text(f'{month}')
birthday_input_Day = Select(driver.find_element(By.CSS_SELECTOR,"select[title='Day:']"))
birthday_input_Day.select_by_visible_text(f'{date}')
birthday_input_year = Select(driver.find_element(By.CSS_SELECTOR,"select[title='Year:']"))
birthday_input_year.select_by_visible_text(f'{year}')
sleep(3)
driver.find_element(By.XPATH,"//button[normalize-space()='Next']").click()
print("month button clicker")
sleep(5)
print('birthdays values filled successfully --------')