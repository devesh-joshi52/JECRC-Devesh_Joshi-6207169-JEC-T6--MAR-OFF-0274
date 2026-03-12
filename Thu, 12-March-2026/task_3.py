from selenium import webdriver
from time import sleep

for browser in [webdriver.Chrome, webdriver.Firefox, webdriver.Edge]:
    driver = browser()
    driver.get("https://www.vlr.gg/")
    sleep(5)

    print(f'Current URL is: {driver.current_url}')
    print(f'Driver name: {driver.name}')
    print(f'Driver title: {driver.title}')
    print('--------------------------------')
    driver.quit()