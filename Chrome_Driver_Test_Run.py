from selenium import webdriver

class ChromeBrowser:

    def open_browser(self):
        driver = webdriver.Chrome()
        driver.get("https://www.ibm.in")

chr = ChromeBrowser()
chr.open_browser()