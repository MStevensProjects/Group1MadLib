#!/bin/python3

# The headless drivers for selenium weren't working in our AWS Linux box.
# this script is abandoned.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
WINDOW_SIZE = "1920,1080"
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
driver.get("http://madlibs.thegoldenducks.click")
title = driver.title
print("title: "+driver.title)

if driver.title == "Madlib":
  print("Test Passed!")
  driver.close()
  sys.exit(0)
else:
  print("Test Failed!")
  driver.close()
  sys.exit(1)
  
driver.close()  
