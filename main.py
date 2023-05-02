from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime

# loading linkedin homepage
driver = webdriver.Chrome(service=webdriver.chrome.service.Service(executable_path=r"C:\Users\DELL\Downloads\chromedriver_win32\chromedriver.exe"))

# linkedIn login page url
url = 'https://www.linkedin.com/home'
driver.get(url)
time.sleep(2)

# signing in
email = driver.find_element("xpath", '//input[@name = "session_key"]')
password = driver.find_element("xpath", '//input[@name = "session_password"]')
with open(r"D:\PythonProjects\LinkedInPostAutomation\usname.txt") as myUser:
    username = myUser.read().replace('\n', '')
email.send_keys(username)
with open(r"D:\PythonProjects\LinkedInPostAutomation\pwd.txt") as myPass:
    passcode = myPass.read().replace('\n', '')
password.send_keys(passcode)
time.sleep(5)

submit = driver.find_element("xpath", '//button[@type = "submit"]').click()
time.sleep(5)

##posting
postarea = driver.find_element("xpath", '//span[text()= "Start a post"]').click()
time.sleep(5)

#testing