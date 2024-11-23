from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Path to the extension
extension_path = r'C:\Users\hp\Documents\insta_create\hikke\tests\SessionBox.crx'

# Initialize Chrome WebDriver with extension
options = Options()
options.add_experimental_option("detach", True)
options.add_extension(extension_path)

driver = webdriver.Chrome(options=options)

# Perform actions using the driver with the extension

# Close the WebDriver
# driver.quit()
