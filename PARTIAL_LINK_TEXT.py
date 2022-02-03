import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Navigate to the webpage


drv = webdriver.Firefox()
drv.maximize_window()
drv.get("http://localhost/practice/")

partial = drv.find_elements(By.PARTIAL_LINK_TEXT,"Forgot")
print(len(partial))