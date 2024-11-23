from time import sleep
import seleniumdriver
from selenium.webdriver.common.by import By
driver = seleniumdriver.undetectable_driver()

  
driver.get('https://www.instagram.com/accounts/emailsignup')
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get("https://10minutesemail.net/")
sleep(5)
mail_address = driver.find_element(By.ID,'i-email').text
print(mail_address,'================this is mail address')
driver.switch_to.window(driver.window_handles[0])

# Accepting cookies window
try:
        cookie = driver.find_element_by_xpath('/html/body/div[4]/div/div/button[1]').click()
except:
        pass
# name = utils.username()

# Fill email
sleep(0.5)
email_field = driver.find_element_by_name('emailOrPhone')
email_field.send_keys(mail_address)
print('email: ' + mail_address)
print('fill email working-------------------')
# fill full name

# fullname_field = driver.find_element_by_name('fullName')
# fullname_field.send_keys(utils.generatingName())
# print('Full name: '+ utils.generatingName())
# #fill username
# username_field = driver.find_element_by_name('username')
# username_field.send_keys(name)
# print('username: ' + name)
first_name = names.get_first_name()
last_name = names.get_last_name()
fullname = first_name + last_name
print("___________+++",fullname,type(fullname))
fullname_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,"//input[@name='fullName']")))
fullname_field.send_keys(fullname)

#fill username
username = first_name+'_'+last_name+"__"+str(random.randint(0,1000))
print('________________-username',username)
username_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME,'username')))
username_field.send_keys(username)
# Fill password 

# password_field = driver.find_element_by_name('password')
# password_field.send_keys(utils.generatePassword())  # You can determine another password here.
password = utils.generatePassword()
# sumbit = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/form/div[7]/div/button"))).click()
print('password: ' + password)
password_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME,'password')))
password_field.send_keys(password)  # You can determine another password here.
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,'//button[contains(text(), "Sign up")]'))).click()
# signup_button.click()
sleep(5)
print('signup - button clicked-----------')
unavail_mess = ["A user with that username already exists.", "This username isn't available. Please try another."]
sleep(1.2)
# New username if unavailable
try :
        unavailable_user = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[8]/p').text
        if unavailable_user in unavail_mess: 
                print('username unavailable. Generating a new username...')
                username_clear = driver.find_element(By.NAME,"username").clear()
                sleep(1)
                username_field.send_keys(first_name+'_'+last_name+"__"+random.randint(0,1000),Keys.ENTER)
                # driver.find_element_by_xpath('/html/body/div[1]/div/div/section/main/div/div/div[1]/div[2]/form/div[7]/div/button').click()
                WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,'//button[contains(text(), "Sign up")]'))).click()

        else :

                None
except:

        pass


# Birthdate values 
# birthday section
birthday_input = Select(driver.find_element(By.CSS_SELECTOR,"select[title='Month:']"))
birthday_input.select_by_visible_text('February')
birthday_input_Day = Select(driver.find_element(By.CSS_SELECTOR,"select[title='Day:']"))
birthday_input_Day.select_by_visible_text('14')
birthday_input_year = Select(driver.find_element(By.CSS_SELECTOR,"select[title='Year:']"))
birthday_input_year.select_by_visible_text('2000')
sleep(3)
driver.find_element(By.XPATH,"//button[normalize-space()='Next']").click()
print("month button clicker")
sleep(5)
print('birthdays values filled successfully --------')

# Requesting the verification code

print("Waiting for the verification code...")
driver.switch_to.window(driver.window_handles[1])
sleep(30)
# driver.execute_script("window.scrollTo(0, Y)")
#----------------------------------------------------------------
mmms = driver.find_element_by_xpath("/html[1]/body[1]/main[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[2]").text
print('+++++++++=((((((((((((((((((',mmms)
while mmms == "If you receive any email, it will be shown in here!":
        mmms = driver.find_element(By.XPATH,"/html[1]/body[1]/main[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[2]").text

else:
        mmms = mmms

sleep(30)
code = mmms[:6]
print("Confirmation Code is: "+ code)

driver.switch_to.window(driver.window_handles[0])

# Security code  
driver.find_element_by_name('email_confirmation_code').send_keys(code, Keys.ENTER)
sleep(5)

try:
        not_valid = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[4]/div')
        if not_valid.text == 'That code isn\'t valid. You can request a new one.' :

                sleep(1)
                driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[1]/div[2]/div/button').click()
                sleep(5)
                confInput = driver.find_element_by_name('email_confirmation_code')
                confInput.send_keys(Keys.CONTROL + "a")
                confInput.send_keys(Keys.DELETE)
                confInput.send_keys(code, Keys.ENTER)
                sleep(3)
        else:
                print('Account created information stored on a credentials.txt ')
except:
        pass
with open('credentials/credentials.txt','a') as f:
        f.write(f"""\nEmail: {mail_address}\nUsername: {username}\nPassword:{password}\n  -----------""")