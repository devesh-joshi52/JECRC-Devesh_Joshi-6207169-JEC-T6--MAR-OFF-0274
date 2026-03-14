from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()

username = driver.find_element(By.XPATH, "//input[@name='username']")
print("Username field found:", username)

password = driver.find_element(By.XPATH, "//input[@id='password']")
print("Password field found:", password)

login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
print("Login button found:", login_button)

elemental_link = driver.find_element(By.XPATH, "//a[text()='Elemental Selenium']")
print("Elemental Selenium link found:", elemental_link)

heading = driver.find_element(By.XPATH, "//h2[contains(text(),'Login')]")
print("Heading found:", heading)

sleep(5)
driver.quit()