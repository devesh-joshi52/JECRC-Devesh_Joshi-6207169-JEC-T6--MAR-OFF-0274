from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

radio_buttons = driver.find_elements(By.NAME, "gender")

for radio in radio_buttons:
    value = radio.get_attribute("value")
    print("Radio Button:", value)

driver.quit()