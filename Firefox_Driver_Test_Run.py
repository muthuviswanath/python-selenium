from selenium import webdriver


class FirefoxBrowser:

    def open_browser(self):
        driver = webdriver.Firefox()
        driver.get("https://www.pentagonspace.in")


chr = FirefoxBrowser()
chr.open_browser()

