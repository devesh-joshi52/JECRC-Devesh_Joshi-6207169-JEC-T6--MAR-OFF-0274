from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get(r"C:\Users\jdeve\OneDrive\Desktop\Python-Capg\Capgemini_training\index1.html")
driver.maximize_window()
action = ActionChains(driver)

driver.find_element(By.ID, 'password').send_keys("dsp")
sleep(3)

show_pass = driver.find_element(By.ID, 'eyeBtn')
action.click_and_hold(show_pass).perform()
sleep(3)

action.release().perform()
sleep(3)

