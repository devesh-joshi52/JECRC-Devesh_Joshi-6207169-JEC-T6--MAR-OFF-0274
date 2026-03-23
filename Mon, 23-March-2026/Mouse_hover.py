from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = webdriver.Chrome()
driver.get("https://supertails.com/")
driver.maximize_window()
action = ActionChains(driver)


dog = driver.find_element(By.XPATH, '(//span[contains(text(),"Dog")])[1]')
sleep(3)
action.move_to_element(dog).perform()
sleep(4)
