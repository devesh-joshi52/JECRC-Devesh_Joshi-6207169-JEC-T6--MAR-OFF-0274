from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get("https://www.amazon.in/")
driver.maximize_window()

driver.implicitly_wait(10)

search_bar = driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")
print("Search bar found:", search_bar)

logo = driver.find_element(By.CSS_SELECTOR, "#nav-logo")
print("Amazon logo found:", logo)

cart = driver.find_element(By.CSS_SELECTOR, "#nav-cart")
print("Cart found:", cart)

signin = driver.find_element(By.CSS_SELECTOR, "#nav-tools a")
print("Sign in link found:", signin)

categories = driver.find_elements(By.CSS_SELECTOR, "#nav-xshop a")

print("Number of category links:", len(categories))

for cat in categories:
    print(cat.text)

sleep(5)
driver.quit()