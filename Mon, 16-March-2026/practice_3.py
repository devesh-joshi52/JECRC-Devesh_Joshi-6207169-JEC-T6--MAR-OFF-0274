from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()

days = driver.find_elements(By.XPATH, "//div[@class='form-check form-check-inline']/input[@type ='checkbox']")
a = len(days)

for i in days:
    i.click()
    sleep(1)
    print(i.get_attribute('value'))
    sleep(1)

for i in days[::-1]:
    i.click()
    sleep(1)

driver.quit()