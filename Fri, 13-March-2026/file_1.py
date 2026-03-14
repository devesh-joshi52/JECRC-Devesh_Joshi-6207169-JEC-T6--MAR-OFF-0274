from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
# opts.add_argument('--headless')
driver = webdriver.Chrome(options=opts)

driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(2)

# print('Completed')

# name = driver.find_element(By.ID, 'name')
# print(name)
# print('Name textfield found')

# phone_no = driver.find_element(By.ID, 'phone')
# print(phone_no)
# print('Phone_no textfield found')

# nav_bar = driver.find_element(By.NAME, 'Navbar')
# print(nav_bar)
# print('Navbar textfield found')

# radio_button = driver.find_elements(By.CLASS_NAME, 'form-check-input')
# print(radio_button)
# print(len(radio_button))
# print('Radio button textfield found')

# inp = driver.find_element(By.TAG_NAME, 'input')
# print(inp)

name = driver.find_element(By.CSS_SELECTOR, '#animals')
print(name)
print("worked fine")
driver.quit()
