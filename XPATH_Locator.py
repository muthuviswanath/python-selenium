import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Navigate to the webpage


drv = webdriver.Firefox()
drv.maximize_window()
drv.get("http://localhost/practice/")

#Find elements by xpath
my_name = drv.find_element(By.XPATH,"//input[@id='name']")
my_name.send_keys(input("Enter the name: "))
alrt = drv.find_element(By.XPATH,"//input[@id='alertbtn']")
alrt.click()