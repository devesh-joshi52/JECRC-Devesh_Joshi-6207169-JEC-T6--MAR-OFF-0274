from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/windows')
sleep(3)
driver.maximize_window()
sleep(3)

parent_window = driver.current_window_handle
sleep(2)

driver.find_element(By.XPATH, '//a[text()="Click Here"]').click()
sleep(3)
all_windows = driver.window_handles
print(len(all_windows))

driver.switch_to.window(all_windows[-1])
sleep(3)

# print(driver.find_element(By.CLASS_NAME, 'example').text)
assert 'New' in driver.find_element(By.CLASS_NAME, 'example').text
print('done')
sleep(3)

driver.switch_to.window(parent_window)
sleep(4)

