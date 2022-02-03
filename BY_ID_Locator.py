import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Navigate to the webpage


drv = webdriver.Firefox()
drv.maximize_window()
drv.get("http://localhost/practice/")

# Find Elements by ID only

radio_select = drv.find_element(By.ID, "pythonradio")
radio_select.click()
time.sleep(5)
print("Python Radio button is selected")

python_check_box = drv.find_element(By.ID, "pythoncheck")
python_check_box.click()
time.sleep(5)
print("Python check box is selected")

selenium_check_box = drv.find_element(By.ID, "seleniumcheck")
selenium_check_box.click()
time.sleep(5)
print("Selenium check box is selected")

appium_check_box = drv.find_element(By.ID, "appiumcheck")
appium_check_box.click()
time.sleep(5)
print("Appium check box is selected")

name_text_box = drv.find_element(By.ID, "name")
name_text_box.send_keys("Yogi, Hareesh and Praveen")
time.sleep(5)
print("Names have been typed into the name text box")

display_text_box = drv.find_element(By.ID, "displayed-text")
display_text_box.send_keys("Welcome to Pentagon Space")
time.sleep(5)
print("Message have been typed into the name text box")
hide_element = drv.find_element(By.ID, "hide-textbox")
hide_element.click()
time.sleep(5)
print("Text box is now hidden")
show_element = drv.find_element(By.ID, "show-textbox")
show_element.click()
time.sleep(5)
print("Text box is now shown")
