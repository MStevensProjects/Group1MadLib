#!/bin/python3
  
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
driver.close()

if driver.title == "Madlib":
  print("Test Passed!")
  return 0
else:
  print("Test Failed!")
  return 1
