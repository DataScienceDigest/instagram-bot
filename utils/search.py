
# sleep(25)
def search():
    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CSS_SELECTOR,"[aria-label='Search']"))).click() _2vDPL
    print('search clicked')
    username = 'rohit_yadav_0_'
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

    sleep(5)
    driver.get(f'https://www.instagram.com/{username}/followers/')
    # driver.find_element(By.XPATH,"//span[contains(., 'followers')]").click()
    sleep(10)
    print('followers clicked')
    # for butt in followButtons:
    #     butt.click()
#_______________________________________________________________________________________
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
    # driver.get(f'https://www.instagram.com/{username}/hashtag_following/')
        # btn.click()

        # else:
        #         continue
        # folllow by hashtag following or by similar accoutns
        # https://www.instagram.com/sk3354580/hashtag_following/
    # https://www.instagram.com/official_bobby_bhagat786/hashtag_following/
#_______________________________________
# for i in abc:
#      if i.text == 'Follow':
#         driver.execute_script("arguments[0].click();", i)
            
        print("______________completed__________________________")
search()
