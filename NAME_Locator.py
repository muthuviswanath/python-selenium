import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Navigate to the webpage


drv = webdriver.Firefox()
drv.maximize_window()
drv.get("http://localhost/practice/")

# Identify the elements using name locator
text_place = drv.find_element(By.NAME,"enter-name")
text_place.send_keys("Yogi")