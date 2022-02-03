import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Navigate to the webpage


drv = webdriver.Firefox()
drv.maximize_window()
drv.get("http://localhost/practice/")

#Find Elements by Tagname
cli = drv.find_elements(By.TAG_NAME,"input")
print(len(cli))