import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Navigate to the webpage


drv = webdriver.Firefox()
drv.maximize_window()
drv.get("http://localhost/practice/")

#CSS Selector

name_text = drv.find_element(By.CSS_SELECTOR,"#name")
name_text.send_keys(input("Enter the name: "))
alert_btn = drv.find_element(By.CSS_SELECTOR,"#alertbtn")
alert_btn.click()