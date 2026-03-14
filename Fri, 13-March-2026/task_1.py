from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get("https://www.cricbuzz.com/")
driver.maximize_window()

driver.implicitly_wait(10)

# ID locator
logo = driver.find_element(By.ID, "cb-logo-main-menu")
print("ID locator found:", logo)

# Class Name locator
header = driver.find_element(By.CLASS_NAME, "cb-header")
print("Class locator found:", header)

# Tag Name locator
body_tag = driver.find_element(By.TAG_NAME, "body")
print("Tag locator found:", body_tag)

# Link Text locator
live_scores = driver.find_element(By.LINK_TEXT, "Live Scores")
print("Link Text found:", live_scores)

# Partial Link Text locator
series = driver.find_element(By.PARTIAL_LINK_TEXT, "Series")
print("Partial Link Text found:", series)

# XPath locator
xpath_locator = driver.find_element(By.XPATH, "//a[text()='Live Scores']")
print("XPath found:", xpath_locator)

# CSS Selector locator
css_locator = driver.find_element(By.CSS_SELECTOR, "a[href='/cricket-match/live-scores']")
print("CSS Selector found:", css_locator)

sleep(5)
driver.quit()