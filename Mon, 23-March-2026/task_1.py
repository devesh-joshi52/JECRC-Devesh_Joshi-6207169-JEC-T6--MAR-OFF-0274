from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.royalchallengers.com/")
driver.maximize_window()
action = ActionChains(driver)

sleep(2)
picture = driver.find_element(By.XPATH, "(//img[@alt='Rajat Patidar'])[3]")
action.scroll_to_element(picture).perform()
sleep(5)

for i in range(0,4):
    action.send_keys(Keys.PAGE_UP).perform()
    sleep(1)
sleep(5)
driver.quit()