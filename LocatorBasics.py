from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("file:///D:/AutomationTesting/Index.html")

username = driver.find_element(By.ID, "user")
username.send_keys("Test")

username = driver.find_element(By.ID,"pass")
username.send_keys("admin")

forgotlink = driver.find_element(By.LINK_TEXT, "Forgot Password?")
forgotlink.click()
