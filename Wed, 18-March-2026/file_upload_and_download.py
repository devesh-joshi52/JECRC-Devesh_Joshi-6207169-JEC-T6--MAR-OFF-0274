from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
# driver.get('https://the-internet.herokuapp.com/upload')
# driver.maximize_window()
# sleep(3)
#
# choose_file = driver.find_element(By.ID, 'file-upload')
# choose_file.send_keys(r"C:\Users\jdeve\Downloads\WhatsApp Image 2026-02-18 at 2.06.19 PM.jpeg")
#
# submit_button = driver.find_element(By.ID, 'file-submit')
# submit_button.click()
# sleep(5)


driver.get('https://the-internet.herokuapp.com/download')
driver.maximize_window()
sleep(3)

driver.find_element(By.XPATH, '//a[text()="playwright_advanced_demo.py"]').click()
sleep(10)

print("downloaded")
