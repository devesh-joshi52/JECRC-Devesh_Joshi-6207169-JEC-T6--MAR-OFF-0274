from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()

driver.get("https://www.flipkart.com/")
driver.maximize_window()


sleep(2)

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("laptop")
search_box.send_keys(Keys.RETURN)

sleep(3)


checkbox = driver.find_element(By.XPATH, "//div[text()='Dual Core']/ancestor::label")
checkbox.click()

sleep(5)

print("Selected Filter:", checkbox.text)

sleep(5)

driver.quit()