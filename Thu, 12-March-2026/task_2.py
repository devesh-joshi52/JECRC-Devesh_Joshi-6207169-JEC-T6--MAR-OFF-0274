from selenium import webdriver
from time import sleep

for browser in [webdriver.Chrome, webdriver.Firefox, webdriver.Edge]:
    driver = browser()
    driver.get("https://www.vlr.gg/")
    sleep(5)
    driver.quit()