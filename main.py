from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 


import pandas as pd

driver = webdriver.Firefox()

driver.get("https://web.whatsapp.com")
wait = WebDriverWait(driver, 600)

xyz = input()


# Target Name
target = "Didi"

# Message to be sent
string = "Message sent using Python!!!"

x_arg = "//span[contains(@title,'" + target + "')]"
print(x_arg)

group_title = wait.until(EC.presence_of_element_located((
    By.XPATH, x_arg)))

#print(group_title)
#import pdb; pdb.set_trace()

group_title.click()

string = "Test code to be sent"

inp_xpath = '//div[contains(@class,"selectable-text")]'
input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
for i in range(10):
    input_box.send_keys(string + Keys.ENTER)
    time.sleep(1)
    print("Input Sent")

