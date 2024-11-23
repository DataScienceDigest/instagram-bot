# import random
# test_list = ['January','February','March','April','May','June','July','August','September','October','November','December']
# random_num = random.choice(test_list)
# print(random_num)
# date = random.randint(1,30)
# year = random.randint(1990,2004)
# print(date,random_num,year)
# for i in range(5):
#     print(i)

# login()
# update_profile()
# follow_suggested()
# upload_posts()
# do_likes_follow()
# here i have some string
# i = 'password'
# while i == 'password': # while loop until the i is equl to the string
#   print(i)
#   i = input('enter new name:')
# else:
#   print("new name is ",i)

# Python program to demonstrate
# writing to CSV


# import csv
	
# # field names
# fields = ['email', 'password']
	
# # data rows of csv file
# rows = [ ['Nikhil', 'COE'],
# 		['Sahil', 'EP']]
	
# # name of csv file
# filename = "university_records.csv"
	
# # writing to csv file
# with open(filename, 'w') as csvfile:
# 	# creating a csv writer object
# 	csvwriter = csv.writer(csvfile)
		
# 	# writing the fields
# 	csvwriter.writerow(fields)
		
# 	# writing the data rows
# 	csvwriter.writerows(rows)

# ss = 'shiv'
# print("//*[contains(text(),'{}')]".format(ss))
# import os
# import random 
# directory = "imagesss"
# path = r'C:\Users\hp\Documents\insta_create\hikke\imagesss'
# files=os.listdir(path)
# d=random.choice(files)
# print(d,'afdsgfds')
# pathname = r"C:\Users\hp\Documents\insta_create\hikke\imagesss\{}".format(d)
# print(pathname)

# importing geopy library
# from geopy.geocoders import N..

# calling the Nominatim tool
# loc = Nominatim(user_agent="GetLoc")

# # entering the location name
# getLoc = loc.geocode("Gosainganj Lucknow")

# # printing address
# print(getLoc.address)

# # printing latitude and longitude
# print("Latitude = ", getLoc.latitude, "\n")
# print("Longitude = ", getLoc.longitude)
# Latitude & Longitude input
# Latitude = "31.34268275"
# Longitude = "75.53593825"

# location = geolocator.reverse(Latitude+","+Longitude)

# # Display
# print(location)


# import indian_names

# print(indian_names.get_full_name(gender='female'))
# grinning face
# import emoji module
# import emoji
# from IndianNameGenerator import *
# print(randomPunjabi())
# print(malePunjabi())
# print(femalePunjabi())
# print(emoji.)
# print(emoji.emojize(":grinning_face_with_big_eyes:"))
# print(emoji.emojize(":winking_face_with_tongue:"))
# print(emoji.emojize(":zipper-mouth_face:"))


# from itertools import accumulate
# from bisect import bisect
# from random import randrange
# from unicodedata import name as unicode_name

# # Set the unicode version.
# # Your system may not support Unicode 7.0 charecters just yet! So hipster.
# UNICODE_VERSION = 6

# # Sauce: http://www.unicode.org/charts/PDF/U1F300.pdf
# EMOJI_RANGES_UNICODE = {
#     6: [
#         ('\U0001F300', '\U0001F320'),
#         ('\U0001F330', '\U0001F335'),
#         ('\U0001F337', '\U0001F37C'),
#         ('\U0001F380', '\U0001F393'),
#         ('\U0001F3A0', '\U0001F3C4'),
#         ('\U0001F3C6', '\U0001F3CA'),
#         ('\U0001F3E0', '\U0001F3F0'),
#         ('\U0001F400', '\U0001F43E'),
#         ('\U0001F440', ),
#         ('\U0001F442', '\U0001F4F7'),
#         ('\U0001F4F9', '\U0001F4FC'),
#         ('\U0001F500', '\U0001F53C'),
#         ('\U0001F540', '\U0001F543'),
#         ('\U0001F550', '\U0001F567'),
#         ('\U0001F5FB', '\U0001F5FF')
#     ],
#     7: [
#         ('\U0001F300', '\U0001F32C'),
#         ('\U0001F330', '\U0001F37D'),
#         ('\U0001F380', '\U0001F3CE'),
#         ('\U0001F3D4', '\U0001F3F7'),
#         ('\U0001F400', '\U0001F4FE'),
#         ('\U0001F500', '\U0001F54A'),
#         ('\U0001F550', '\U0001F579'),
#         ('\U0001F57B', '\U0001F5A3'),
#         ('\U0001F5A5', '\U0001F5FF')
#     ],
#     8: [
#         ('\U0001F300', '\U0001F579'),
#         ('\U0001F57B', '\U0001F5A3'),
#         ('\U0001F5A5', '\U0001F5FF')
#     ]
# }

# # NO_NAME_ERROR = '(No name found for this codepoint)'

# # def random_emoji(unicode_version = 6):
# #     if unicode_version in EMOJI_RANGES_UNICODE:
# #         emoji_ranges = EMOJI_RANGES_UNICODE[unicode_version]
# #     else:
# #         emoji_ranges = EMOJI_RANGES_UNICODE[-1]

# #     # Weighted distribution
# #     count = [ord(r[-1]) - ord(r[0]) + 1 for r in emoji_ranges]
# #     weight_distr = list(accumulate(count))

# #     # Get one point in the multiple ranges
# #     point = randrange(weight_distr[-1])

# #     # Select the correct range
# #     emoji_range_idx = bisect(weight_distr, point)
# #     emoji_range = emoji_ranges[emoji_range_idx]

# #     # Calculate the index in the selected range
# #     point_in_range = point
# #     if emoji_range_idx != 0:
# #         point_in_range = point - weight_distr[emoji_range_idx - 1]

# #     # Emoji 😄
# #     emoji = chr(ord(emoji_range[0]) + point_in_range)
# #     emoji_name = unicode_name(emoji, NO_NAME_ERROR).capitalize()
# #     emoji_codepoint = "U+{}".format(hex(ord(emoji))[2:].upper())

# #     return (emoji)

# # ss =  random_emoji(UNICODE_VERSION)
# # print('_.'+ss,type('_.'+ss))

# # import ipaddress
# # # initialize an IPv4 Address
# # ip = ipaddress.IPv4Address("192.168.1.1")
# # print(ip)
# import pixabay.core

# # init pixabay API
# px = pixabay.core("E6FmwPmIhSYCHaBousGztWN08B9lgy2d316QMrhv95rsCcOQvbLIa1fM ")

# # search for space
# space = px.query("flower")

# # get len of hits len(space)
# print("{} hits".format(len(space)))

# # downalod fisrt image
# # space[0].download("space.jpg")
# from tempmail import TempMail

# tm = TempMail()
# email = tm.get_email_address()  # v5gwnrnk7f@gnail.pw
# print(tm.get_mailbox(email))
# @gfg_decorator
