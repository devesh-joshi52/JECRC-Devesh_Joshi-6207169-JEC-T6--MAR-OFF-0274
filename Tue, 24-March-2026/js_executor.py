from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.get("https://in.pinterest.com/")
driver.maximize_window()
sleep(3)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
sleep(3)

driver.execute_script("window.scrollTo(0,0)")
sleep(3)

driver.execute_script("window.scrollBy(0,500)")
sleep(2)
driver.execute_script("window.scrollBy(0,-200)")
sleep(3)


#scroll to element
element = driver.find_element(By.XPATH, "(//div[@class='ADXRXN gEQpi5']/descendant::img)[13]")
driver.execute_script("arguments[0].scrollIntoView()", element)
sleep(3)

#clicking
click_ele = driver.find_element(By.XPATH, "(//div[@class='lIkAnG eMU5i5 o5UlW_ hL1e7w'])[4]")
driver.execute_script("arguments[0].click();", click_ele)
sleep(3)