from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = webdriver.Chrome()
driver.get(r"C:\Users\jdeve\OneDrive\Desktop\Python-Capg\Capgemini_training\address.html")
driver.maximize_window()
action = ActionChains(driver)

present = driver.find_element(By.ID, 'presentAddress')
permanent = driver.find_element(By.ID, 'permanentAddress')

present.send_keys('JECRC, Jaipur, RJ')
sleep(2)
present.click()

action.key_down(Keys.CONTROL).send_keys('a').perform()
sleep(1)
action.key_down(Keys.CONTROL).send_keys('c').perform()
sleep(1)

permanent.click()
action.key_down(Keys.CONTROL).send_keys('v').perform()
sleep(2)