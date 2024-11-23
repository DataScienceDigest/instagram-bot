from seleniumdriver import undetectable_driver
from tor_browser import tor_driver
from .main2 import generate_password
from mailtm import Email
import re
from time import sleep
import random
import names
import indian_names
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
def desktop_account_create(total_accounts):
        for i in range(total_accounts):
                # driver = tor_driver() # tor driver firefox
                driver =  undetectable_driver()
                # -----------------------------------------------------------------------------
                driver.get('https://www.instagram.com/accounts/signup/email/')
                try:
                        sleep(5)
                        cookie = driver.find_element(By.XPATH,'//button[contains(text(), "Decline optional cookies")]').click()
                        sleep(5)
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

                                # driver.switch_to.window(driver.window_handles[0])

                                # Security code  
                                enter_code = driver.find_element(By.NAME,'email_confirmation_code')
                                enter_code.send_keys(code, Keys.ENTER)
                                listening = False  # Set the flag to stop listening
                                

                
                mail_address = str(test.address)
                test.start(listener)

                print(mail_address,'-=-=-=-=-=-=')

                print('comes here----------------')
                sleep(random.randint(1,5))
                # email_field = driver.find_element(By.NAME,"email")  #for phone
                email_field = driver.find_element(By.NAME,"emailOrPhone") # for desktop
                email_field.send_keys(mail_address)
                print('email: ' + mail_address)
                # fill full name

                first_name = names.get_first_name()
                last_name = names.get_last_name()
                fullname = first_name + last_name
                print("___________+++",fullname,type(fullname))
                fullname_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,"//input[@name='fullName']")))
                sleep(random.randint(1,5))
                fullname_field.send_keys(fullname)

                #fill username
                username = first_name+'_'+last_name+"__"+str(random.randint(0,1000))
                print('________________-username',username)
                username_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME,'username')))
                sleep(random.randint(1,5))
                username_field.send_keys(username)

                # Fill password 
                print('working till here-=-=-')
                # password_field = driver.find_element_by_name('password')
                # password_field.send_keys(utils.generatePassword())  # You can determine another password here.
                password = generate_password()
                # sumbit = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/form/div[7]/div/button"))).click()
                print('password: ' + password)
                password_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME,'password')))
                sleep(random.randint(1,5))
                password_field.send_keys(password)  # You can determine another password here.
                WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,'//button[contains(text(), "Next")]'))).click()
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

                # Requesting the verification code
                
                print("Waiting for the verification code...")
                while listening:
                        pass  # Do nothing while listening
                # test.stop()
                print("Code:", code)
        
                print("Confirmation Code is: "+ code)

                # driver.switch_to.window(driver.window_handles[0])

                # Security code  
                # enter_code = driver.find_element(By.NAME,'email_confirmation_code')
                # enter_code.send_keys(code, Keys.ENTER)
                # driver.find_element_by_name('email_confirmation_code').send_keys(code, Keys.ENTER)
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
                with open('credentials.txt','a') as f:
                        f.write(f"""\nEmail: {mail_address}\nUsername: {username}\nPassword:{password}\n  -----------""")
                # -----------------------------------------------------------------------------

desktop_account_create(2)
# --------------------------------------accoutn create done----------------------