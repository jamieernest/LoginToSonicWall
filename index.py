from selenium import webdriver
import yaml
import os
from time import sleep

conf = yaml.safe_load(open('loginDetails.yml'))
username = conf['sonicwallLogin']['username']
password = conf['sonicwallLogin']['password']
url = conf['sonicwallLogin']['url']

driver = webdriver.Chrome()

def login(url,usernameId, username, passwordId, password, submit_buttonId):
   driver.get(url)
   driver.implicitly_wait(15)
   driver.find_element("name", usernameId).send_keys(username)
   driver.find_element("name", passwordId).send_keys(password)
   driver.find_element("name", submit_buttonId).click()


for i in range(10):
   login(url, "userName", username, "pwd", password, "Submit")
   sleep(3600)
driver.quit()
sleep(10)
os.system("python index.py")