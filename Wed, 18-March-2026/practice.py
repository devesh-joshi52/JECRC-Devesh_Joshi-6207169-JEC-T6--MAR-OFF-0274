from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.lenskart.com/')
driver.maximize_window()

sunglasses = driver.find_element(By.ID, 'lrd5').click()
sleep(5)

sort_by_dropdown = driver.find_element(By.ID, 'sortByDropdown')
dropdown = Select(sort_by_dropdown)

dropdown.select_by_value('saving')
sleep(5)

first_element = driver.find_element(By.XPATH, '(//div[@class="sc-bf32d8a7-0 gOVKHN"])[1]/descendant::p[@class = "sc-23b7d3eb-2 dQrJBg"][1]')
print(first_element.text)
sleep(5)

driver.quit()