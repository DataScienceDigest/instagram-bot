# from mailtm import Email
# import re

# test = Email()
# code = None
# listening = True  # Add a flag to control the listener

# def listener(message):
#     global code
#     global listening

#     print("\nSubject: " + message['subject'])
#     code = message['subject']
#     match = re.search(r'\d{6}', code)
#     if match:
#         code = match.group()
#         listening = False  # Set the flag to stop listening

# test.register()
# print("\nEmail Address: " + str(test.address))

# # Start listening
# test.start(listener)

# # Poll for changes in the 'listening' flag to determine when to stop
# while listening:
#     pass  # Do nothing while listening
# # test.stop()
# print("Code:", code)  # Code is now available, and the listener has stopped


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# import requests
# import re
# import time

# # Function to create a temporary email address
# def create_temp_email():
#     response = requests.get("https://tempmailo.com/")
#     print(response.text)
#     with open('new.txt', "w", encoding="utf-8") as file:
#         file.write(response.text)
# create_temp_email()
