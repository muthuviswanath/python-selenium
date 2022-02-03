import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#Navigate to facebook.com
drv = webdriver.Firefox()
baseUrl = "https://www.facebook.com/"
drv.get(baseUrl)
time.sleep(10)

#Login
userName = drv.find_element(By.ID, "email")
userName.send_keys("muthuvenkatfromindia@gmail.com")

password = drv.find_element(By.ID, "pass")
password.send_keys("Pdntspa0!")

loginButton = drv.find_element(By.NAME, "login")
loginButton.click()
time.sleep(10)
#View Profile

dropDown = drv.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/span[1]/div[1]/div[1]")
dropDown.click()
time.sleep(10)

time.sleep(10)
profile_link = drv.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]")
profile_link.click()

#Logout
logoutDropdown = drv.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/span[1]/div[1]/div[1]")
logoutDropdown.click()

logout = drv.find_element(By.XPATH,"//span[contains(text(),'Log Out')]")
logout.click()