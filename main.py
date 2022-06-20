import configparser
import time 
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys




config = configparser.ConfigParser()
config.read("config.ini")

username = config["USER"]["username"]
password = config["USER"]["password"]
userlink = config["USER"]["userlink"]

regex = r"watch|groups|photo|notification|bookmark|gaming|marketplace|stories|friends|"+username

browser = webdriver.Firefox()
browser.implicitly_wait(config['internetspeed']["wait"]) # seconds

browser.get('https://facebook.com')

body = browser.find_element(By.CSS_SELECTOR, "body")
body.send_keys(username, Keys.TAB)
body.send_keys(password, Keys.TAB)
submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")


submit.send_keys("", Keys.ENTER)

time.sleep(5)

# LOGGED IN

browser.get(userlink+ "/following")

time.sleep(5)







links = browser.find_elements(By.CSS_SELECTOR, "a")

link_list = []
for link in links:
    href = link.get_attribute('href')
    if not re.search(regex, href) and len(href) > 25:
        link_list.append(href)

# Make unique
link_list = list(set(link_list))
link_list.sort()

for href in link_list:
    with open("links.txt", 'a') as file:
        file.write(href+"\n" )


time.sleep(2)

browser.quit()








