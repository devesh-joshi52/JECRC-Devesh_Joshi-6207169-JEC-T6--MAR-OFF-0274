from operator import truediv

from selenium import webdriver
from selenium.webdriver.common.by import By


opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# first_input = driver.find_element(By.XPATH, "(//input)[@id='name']")
# print("First input field found:", first_input)
# print()
# second_input = driver.find_element(By.XPATH, "(//input)[@id='email']")
# print("Second input field found:", second_input)
# print()
# third_input = driver.find_element(By.XPATH, "(//input)[@id='phone']")
# print("Third input field found:", third_input)
# print()
# first_radio = driver.find_element(By.XPATH, "(//input[@type='radio'])[1]")
# print("First radio button found:", first_radio)
# print()
# second_checkbox = driver.find_element(By.XPATH, "(//input[@type='checkbox'])[2]")
# print("Second checkbox found:", second_checkbox)

##innerpath
first_ipath = driver.find_element(By.XPATH, "(//a[text()='Home'])")
print(first_ipath.text)
print()
second_ipath = driver.find_element(By.XPATH, "(//a[text()='PlaywrightPractice'])")
print(second_ipath.text)
print()
third_ipath = driver.find_element(By.XPATH, "(//a[text()='Online Trainings'])")
print(third_ipath.text)
print()

elements = driver.find_elements(By.XPATH, "//a[contains(text(),'Japan')]")
print(elements)
driver.quit()