from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = webdriver.Chrome()
driver.get("https://supertails.com/")
driver.maximize_window()
action = ActionChains(driver)
sleep(3)

cat = driver.find_element(By.XPATH, "//div[@data-ganame='Breed 5']")
action.scroll_to_element(cat).perform()
sleep(5)

action.scroll_by_amount(0,-900).perform()
sleep(5)