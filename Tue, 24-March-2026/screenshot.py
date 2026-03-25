import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

folder = os.path.join(os.getcwd(), 'Screenshots')
os.makedirs(folder, exist_ok=True)

driver = webdriver.Chrome()
driver.get("https://in.pinterest.com/")
driver.maximize_window()

action = ActionChains(driver)

sleep(2)

driver.save_screenshot(f'{folder}/full_page.png')
sleep(2)

element = driver.find_element(By.XPATH, "(//div[@class='ADXRXN gEQpi5']/descendant::img)[13]")
# action.scroll_to_element(element).perform()
sleep(2)

element.screenshot(f'{folder}/cherry_red.png')
sleep(2)
