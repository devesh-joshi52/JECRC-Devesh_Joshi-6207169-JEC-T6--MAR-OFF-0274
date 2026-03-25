from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://demo.automationtesting.in/Frames.html')
sleep(3)
driver.maximize_window()

#nested iframe
driver.find_element(By.XPATH, '//a[text()="Iframe with in an Iframe"]').click()

nested_iframe = driver.find_element(By.XPATH, '//iframe[@src="MultipleFrames.html"]')
driver.switch_to.frame(nested_iframe)
sleep(2)

inner_iframe = driver.find_element(By.XPATH, '//iframe[@src="SingleFrame.html"]')
driver.switch_to.frame(inner_iframe)
sleep(2)

driver.find_element(By.XPATH, '//input[@type="text"]').send_keys('123')
sleep(3)

driver.switch_to.parent_frame()
sleep(3)
driver.switch_to.default_content()
sleep(3)