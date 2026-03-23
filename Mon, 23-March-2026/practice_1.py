from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)
driver.get('https://demoqa.com/droppable')
driver.maximize_window()
sleep(3)

#1: Simple
# action = ActionChains(driver)
#
# source = driver.find_element(By.ID, 'draggable')
# target = driver.find_element(By.ID, 'droppable')
#
# action.drag_and_drop(source, target).perform()
# sleep(4)
#
# actual_text = target.text
# expected_text = "Dropped!"
#
#
# assert actual_text == expected_text, f"Test Failed! Expected '{expected_text}', but got '{actual_text}'"
#
# print("Test Passed")

#2: Prevent Propogation
wait = WebDriverWait(driver, 10)
prevent_propogation = wait.until(EC.element_to_be_clickable((By.XPATH,"(//li[@class='nav-item'])[3]//button")))
prevent_propogation.click()

action = ActionChains(driver)

to_drop = driver.find_element(By.ID, 'dragBox')
drop_location_1 = driver.find_element(By.ID, 'notGreedyDropBox')
drop_location_2 = driver.find_element(By.ID, 'notGreedyInnerDropBox')
drop_location_3 = driver.find_element(By.ID, 'greedyDropBoxInner')
drop_location_4 = driver.find_element(By.XPATH, "//div[@id='greedyDropBox']")
sleep(2)

action.drag_and_drop(to_drop, drop_location_1).perform()
sleep(2)
action.drag_and_drop(to_drop, drop_location_2).perform()
sleep(2)
action.drag_and_drop(to_drop, drop_location_3).perform()
sleep(2)
action.drag_and_drop(to_drop, drop_location_4).perform()
sleep(4)


driver.quit()