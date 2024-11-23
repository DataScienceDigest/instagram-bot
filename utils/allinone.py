# ________first phase steps _______________
# 1. login
# 2. update profile
# 3. follow suggested
# 4. do some posts
from main2 import insta_login,update_profile,follow_suggested,do_posts,follow_account,likes_posts,follow_account_followers,account_create
#_______________login________________
username = 'a7e3kpa9cc@email.edu.pl'
password = '~GahWQ8RUP.8'
driver = insta_login(username,password)
print('login step completed')
# update_profile(driver)
print('profile updated successfuly')
# follow_suggested(driver)
print('suggestd follow completed')
# do_posts(driver)
print('posts are submited successfuly')
# follow_account_followers(driver,username)
print('follow accoutn folowers done')


#______________ PHASE 2 START _______________________

# follow_account(driver)
print('follow account done')
# likes_posts(driver)
print('like posts done')

account_create()