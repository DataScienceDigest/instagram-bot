from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import re
from selenium import *
import names
import indian_names
# from emoji import random_emoji
import os
import random
from pathlib import Path
from random import randint
import array
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import random
from selenium_stealth import stealth
import pyautogui
import string
from mailtm import Email
from essential_generators import DocumentGenerator
UNICODE_VERSION = 6
chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_experimental_option('excludeSwitches',["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")
chrome_driver_path = r'C:\Users\hp\Documents\insta_create\hikke\chromedriver.exe'


#______________drivers ______________
def driver_for_account_create():
        # chrome_options.add_argument("--incognito")
        # PROXY = "188.74.210.207:6286"
        # chrome_options.add_argument('--proxy-server=%s' % PROXY)
        # https://deviceatlas.com/blog/list-user-agent-strings-2021 ---------for useragents
        # Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X)AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0Mobile/14E5239e Safari/602.1
        mobile_emulation = {
        "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 4.0 },
        "userAgent": "Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36" 
        }
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        
        # chrome_options.add_argument("--headless=new") # to make headless uncomment this line
        
        driver_account = webdriver.Chrome(options=chrome_options) # Put chrome driver path here!
        # driver_account.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        # "source":
        #         "const newProto = navigator.__proto__;"
        #         "delete newProto.webdriver;"
        #         "navigator.__proto__ = newProto;"
        # })
        stealth(driver_account, 
        # user_agent= r'Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/36.0  Mobile/15E148 Safari/605.1.15',
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win64",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        ) 
        return driver_account

def driver_for_other_tasks():
        driver_tasks = webdriver.Chrome(chrome_driver_path,options=chrome_options) # Put chrome driver path here!
        stealth(driver_tasks,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win64",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        ) 
        return driver_tasks

#___________________________________________________

#___________password Generator _____________________
def generate_password():
    MAX_LEN = 12
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                        'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                        'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                        'z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                        'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                        'Z']

    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
            '*', '(', ')', '<']
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)
    password = ""
    for x in temp_pass_list:
            password = password + x
            
    return password

#__________________________________________________

#  ---------for mobile emulation case ------
def account_create():
        for i in range(10):
                driver = driver_for_account_create()
                driver.get('https://www.instagram.com/accounts/signup/email/')
                driver.execute_script("window.open('');")
                driver.switch_to.window(driver.window_handles[1])
                driver.get("https://10minutesemail.net/")
                sleep(10)
                mail_address = driver.find_element(By.ID,'trsh_mail').get_attribute('value')
                while mail_address == "landing":
                # while mail_address == "Please wait...":
                        sleep(1)
                        print('in while loop')
                        mail_address = driver.find_element(By.ID,'trsh_mail').get_attribute('value')
                        # mail_address = driver.find_element(By.ID,'tempEmailAddress').get_attribute('value')
                # else:
                print(mail_address,'-=-=-=-=-=-=')

                if driver.find_element(By.ID,'trsh_mail').get_attribute('value') != 'landing':

                        mail_address = mail_address
                        driver.switch_to.window(driver.window_handles[0])

                # Accepting cookies window
                try:
                        cookie = driver.find_element(By.XPATH,'/html/body/div[4]/div/div/button[1]').click()
                except:
                        pass
                print('comes here----------------')
                sleep(random.randint(1,5))
                # email_field = driver.find_element(By.NAME,"email")  #for phone
                email_field = driver.find_element(By.NAME,"emailOrPhone") # for desktop
                email_field.send_keys(mail_address)
                print('email: ' + mail_address)
                print('fill email working-------------------')
                WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,'//button[contains(text(), "Next")]'))).click()
                print('next button clicked')
                print("Waiting for the verification code...")
                driver.switch_to.window(driver.window_handles[1])
                sleep(random.randint(15,25))
              
                # value = 'If you receive any email, it will be shown in here!'
                value = 'Waiting for incoming emails'
                print('+++++++++=((((((((((((((((((',value)
                while value == "Waiting for incoming emails":
                        sleep(random.randint(1,5))
                        print(value,'thi is mss data')
                        value = driver.find_element(By.CLASS_NAME,"subject_email").text
                        # value = driver.find_element(By.XPATH,"/html[1]/body[1]/main[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[2]").text
                        
                else:
                        dat = value
                # print(dat, 'the values is-----------')
                sleep(random.randint(5,10))
                code = dat[:6]
                print("Confirmatvdfvdfbvdf: "+ dat,value)

                driver.switch_to.window(driver.window_handles[0])
                # Security code  
                try:
                        driver.find_element(By.NAME,'emailConfirmationCode').send_keys(code)
                        sleep(random.randint(5,10))
                        driver.find_element(By.XPATH,"//button[normalize-space()='Next']").click()
                        first_name = names.get_first_name()
                        last_name = names.get_last_name()
                        full_name = indian_names.get_full_name(gender='female')
                        # fullname = first_name +'_'+ last_name + '__' + str(randint(100,999))
                        fullname = full_name + '__' + str(randint(100,999))
                        print("___________+++",fullname,type(fullname))
                        fullname_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,"//input[@name='fullName']")))
                        sleep(3)
                        fullname_field.send_keys(fullname)
                except:
                        driver.quit()
                print('process for enter name and password----')
                # fill full name
                
                
                print('fill password')
                password = generate_password()
                # sumbit = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/form/div[7]/div/button"))).click()
                print('password: ' + password)
                password_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME,'password')))
                sleep(3)
                password_field.send_keys(password) 
                sleep(random.randint(5,10))
                driver.find_element(By.XPATH,"//button[normalize-space()='Next']").click()
                print('selecting values for birthdays')
                # birthday section
                test_list = ['January','February','March','April','May','June','July','August','September','October','November','December']
                month = random.choice(test_list)
                date = random.randint(1,30)
                year = random.randint(1990,2004)
                print(date,month,year)
                birthday_input = Select(driver.find_element(By.CSS_SELECTOR,"select[title='Month:']"))
                sleep(random.randint(1,4))
                birthday_input.select_by_visible_text(f'{month}')
                birthday_input_Day = Select(driver.find_element(By.CSS_SELECTOR,"select[title='Day:']"))
                sleep(random.randint(1,4))
                birthday_input_Day.select_by_visible_text(f'{date}')
                birthday_input_year = Select(driver.find_element(By.CSS_SELECTOR,"select[title='Year:']"))
                sleep(random.randint(1,4))
                birthday_input_year.select_by_visible_text(f'{year}')
                sleep(random.randint(4,8))
                driver.find_element(By.XPATH,"//button[normalize-space()='Next']").click()
                sleep(random.randint(4,8))
                
                result = ''.join((random.choice(string.ascii_lowercase) for x in range(5)))
                
                username_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,"//input[@name='username']")))
                # ss =  random_emoji(UNICODE_VERSION)
                userlastname = '_'+result
                print(userlastname,')))-----------')
                username_field.send_keys(userlastname)
                sleep(random.randint(4,8))
                
                
                try:
                        driver.find_element(By.XPATH,"//button[normalize-space()='Next']").click()
                        print('waiting for popup')
                        sleep(5)
                        print('if any error click on go back')
                        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,'//button[contains(text(), "Go Back")]'))).click()
                        driver.find_element(By.XPATH,"//button[normalize-space()='Next']").click()
                        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,'//button[contains(text(), "Go Back")]'))).click()
                        print('waiting for popup')
                        sleep(random.randint(5,10))
                        alert = driver.switch_to.alert
                        # #sleep for a second
                        sleep(random.randint(1,5))
                        # #accept the alert
                        alert.accept()
                        print('pop up clicked')
                except:
                        pass
                sleep(random.randint(4,8))
                driver.get('https://www.instagram.com/')
                print('account created successfully',i+1)
                # driver.get('https://www.instagram.com/{username}/')
                with open('credentials.txt','a') as f:
                        f.write(f"""\nEmail: {mail_address}\nUsername: {userlastname}\nPassword: {password}\n  -----------""")
                driver.quit()

# -----------account create using desktop view -----------
       


def insta_login(username,password):
        driver = driver_for_other_tasks()
        url = "https://www.instagram.com/"
        driver.get(url)
        username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME,"username")))
        password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME,"password")))
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,"//button[@type='submit']"))).click()
        print("loged in ")
        return driver


def update_profile(driver):
        path = r'C:\Users\hp\Documents\insta_create\hikke\imagesss'
        files=os.listdir(path)
        d=random.choice(files)
        print(d,'afdsgfds')
        # driver = driver_for_other_tasks()
        WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'//div[@class="x9f619 xxk0z11 xvy4d1p x11xpdln xii2z7h x19c4wfv"]/*[name()="svg"][@aria-label="Home"]'))).click()
        print("home button clicked")
        sleep(10)
        try:
                WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"//button[normalize-space()='Not Now']"))).click()
        except:
                pass
        print("not now clicked")
        WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"//div[@class='_aacl _aacp _aacu _aacx _aada'][normalize-space()='Profile']"))).click()

        # driver.find_element(By.XPATH,"//div[@class='x1n2onr6']//div[@class='x9f619 x3nfvp2 x1z11no5 xjy5m1g x1mnwbp6 x4pb5v6 xr9ek0c xjpr12u xo237n4 x6pnmvc x7nr27j x12dmmrz xz9dl7a xn6708d xsag5q8 x1ye3gou x1l895ks x159b3zp xdoji71 x1v9afh1 x1sxb60h x1ug36kh xubc8zo x1dejxi8 x9k3k5o xs3sg5q x11hdxyr x12ldp4w x1wj20lx x1dn74xm xif99yt x172qv1o x10djquj x1lhsz42 xzauu7c']").click()
        print("profile button clicked")
        sleep(5)
        WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"//a[normalize-space()='Edit profile']"))).click()
        print("edit profile clicked")
        WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"//button[normalize-space()='Change profile photo']"))).click()
        print("change profile clicked")
        pathname = r"C:\Users\hp\Documents\insta_create\hikke\imagesss\{}".format(d)
        print(pathname)
        sleep(5)
        pyautogui.typewrite(pathname)
        print("pyautogui working")
        sleep(5)
        pyautogui.press("enter")
        gen = DocumentGenerator()
        s = gen.sentence()
        print(s)
        driver.find_element(By.XPATH,"//textarea[@id='pepBio']").send_keys(s)
        print("bio added")
        WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"//button[normalize-space()='Submit']"))).click()

        print('profile updated successful')

def follow_suggested(driver):
        # driver = driver_for_other_tasks()
        # WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,'//div[@class="_aacl _aacp _adda _aacx _aada"]'))).click()
        try:
                WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,'//div[@class="x9f619 xxk0z11 xvy4d1p x11xpdln xii2z7h x19c4wfv"]/*[name()="svg"][@aria-label="Home"]'))).click()
        except:
                pass
        print("home button clicked")
        sleep(10)
        # 
        
        try:
                driver.find_element(By.XPATH,"//button[normalize-space()='Not Now']").click()
        except:
                pass
        print("not now clicked")
        # _________ this function works when the account already follow some other accounts 
        # def follow_suggested():
        #         WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,"//div[@class='_aacl _aacn _aacw _aacx _aad6']"))).click()
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
                #print(btn.text)
                if btn.text == 'Follow':
                        
                        sleep(2)
                        btn.click()
                else:
                        continue
                
        print("______________completed__________________________")
        # Use the Java script to click on follow because after the scroll down the buttons will be un clickeable unless you go to it's location
        # driver.execute_script("arguments[0].click();", btn)
        # sleep(3)
        # follow_all()
        print('suggestd follow completed')

#____________________________________________________

def do_posts(driver):
        # directory = "imagesss"
        # folder_path = r'C:\Users\hp\Documents\insta_create\hikke'
        # driver = driver_for_other_tasks()
        #_________read all posts ____________

        # def all_pics():
        #         ls = []
        #         files = Path(directory).glob('*')
        #         for file in files:
        #                 ls.append(file)
        #         return ls
        # pic_data = all_pics()
        # print(pic_data,"-------pic data----------",type(pic_data))

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
                # WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CSS_SELECTOR,"img[alt='Animated checkmark']")))
                WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//div[@class="x78zum5 x6s0dn4 xl56j7k xdt5ytf"]/*[name()="svg"][@aria-label="Close"]'))).click()
                print("close button clicked")
        # for i in pic_data:
        for i in range(10):
                path = r'C:\Users\hp\Documents\insta_create\hikke\imagesss'
                files=os.listdir(path)
                d=random.choice(files)
                print(d)
                z = r"C:\Users\hp\Documents\insta_create\hikke\imagesss\{}".format(d)
                print(z)
                add_button(z)
        print('posts are submited successfuly')

# ______________follow all followers_______________



###################################################################################


####################_______phasse 2 starts here ____________########################


################_______________________________________#############################

def follow_account(driver):
        WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CSS_SELECTOR,"[aria-label='Search']"))).click()
        print('search clicked')
        username = 'sk3354580'
        print(username)
        sleep(5)
        pyautogui.typewrite(username)
        print("pyautogui working")
        sleep(5)
        pyautogui.press("enter")
        print('open pressed')
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,"//*[contains(text(),'{}')]".format(username)))).click()
        sleep(5)
        print('username found successful')
        try:
                WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,"//button[contains(@class,'_acan _acap _acas _aj1-')]//div[@class='_aacl _aaco _aacw _aad6 _aade'][normalize-space()='Follow']"))).click()
        except:
                print('already following ')
        print('following done')
def likes_posts(driver):
        print('likinh the posts')
        ################### for follow the accoutn ##############################
    
        ##########################################################################
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CLASS_NAME,"_aagw"))).click()
        print('posts clicked')
        sleep(10)
        #__++++++++++ liking the post starts here ____________________
        like_ = driver.find_element(By.CSS_SELECTOR,"span._aamw")
        sleep(5)
        element = like_.find_element(By.CSS_SELECTOR,"button._abl-")
        element.click()
        print("like button clicked")
        sleep(10)
        
        #_____________________________working fine _______________________________
        # --------------------this is next post------------------
        s = driver.find_element(By.CSS_SELECTOR,"span[class='_ac2a']")
        t = s.text
        no_of_posts = int(t)
        print(no_of_posts)
        for i in range(no_of_posts):
                if(i>0):
                        next_post = driver.find_element(By.CSS_SELECTOR,"div._aaqg._aaqh")
                        if next_post:
                                print(next_post)
                        else:
                                print('false')
                        sleep(5)
                        ele = next_post.find_element(By.CSS_SELECTOR,"button._abl-")
                        ele.click()
                        sleep(10)
                        like_ = driver.find_element(By.CSS_SELECTOR,"span._aamw")
                        sleep(5)
                        element = like_.find_element(By.CSS_SELECTOR,"button._abl-")
                        element.click()
                        print("like button clicked")
                        sleep(5)
        
        #__________________________________________________________
        # __________ completed__________________________________-_______--
def follow_account_followers(driver,username):
        driver.get(f'https://www.instagram.com/{username}/followers/')
        # driver.find_element(By.XPATH,"//span[contains(., 'followers')]").click()
        sleep(10)
        print('followers clicked')
       #______________________________________________________________________________________
        buttons = WebDriverWait(driver,30).until(EC.presence_of_all_elements_located((By.XPATH,"//button[contains(.,'Follow')]")))
        sleep(10)
        print(len(buttons))
        # driver.execute_script("window.scrollTo(0, Y)")
        for btn in buttons:
                print(btn.text)
                if btn.text == 'Follow':
                        driver.execute_script("arguments[0].click();", btn)
                        sleep(2)
                        print('buton clicked')

#     driver.get(f'https://www.instagram.com/{username}/hashtag_following/')
        # folllow by hashtag following or by similar accoutns
        # https://www.instagram.com/sk3354580/similar_accounts/
    # https://www.instagram.com/official_bobby_bhagat786/hashtag_following/
# account_create()
