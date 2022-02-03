import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Navigate to the webpage


drv = webdriver.Firefox()
drv.maximize_window()
drv.get("http://localhost/practice/")

#Identify elements by classname

elements_count = drv.find_elements(By.CLASS_NAME,"mylinks")
print(elements_count)
print(len(elements_count))