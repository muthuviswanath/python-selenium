import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Navigate to the webpage


drv = webdriver.Firefox()
drv.maximize_window()
drv.get("http://localhost/practice/demo1.html")

# Locate the inputs

# Types of CSS Selector:
# ID
    # <tagname>#<id value>
# CLASS
    # <tagname>.<class name>
# ARRTRIBUTE
    # <tagname>[attribute='attributevalue']
# SUB-STRING
    # Prefix or Starts with
    # <tagname>[attribute^='prefix']

    # Suffix or ends with
    # <tagname>[attribute$='suffix']

    # Match the exact Substring
    # <tagname>[attribute*='substring']

