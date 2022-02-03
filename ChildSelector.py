import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Navigate to the webpage


drv = webdriver.Firefox()
drv.maximize_window()
drv.get("http://localhost/practice/demo1.html")

#Child Selector

div_input = drv.find_element(By.CSS_SELECTOR, "div > input")
div_input.send_keys("Pentagon Space")