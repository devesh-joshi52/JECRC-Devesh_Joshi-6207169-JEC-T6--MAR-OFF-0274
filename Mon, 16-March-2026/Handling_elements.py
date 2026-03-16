from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

name = driver.find_element(By.ID, 'name')
name.clear()
name.send_keys("Devesh")
sleep(1)

email = driver.find_element(By.XPATH, '//input[@placeholder="Enter EMail"]')
email.clear()
email.send_keys("deveshjoshiit54@gmail.com")
sleep(2)

# print(name.get_attribute('placeholder'))
# print(name.get_attribute('value'))

driver.find_element(By.ID, 'male').click()
sleep(2)

driver.find_element(By.XPATH, '//label[text()="Monday"]/preceding-sibling::input').click()
sleep(2)

monday_checkbox = driver.find_element(By.XPATH, '//input[@id="monday"]/following-sibling::label')
monday_checkbox.text()


driver.quit()