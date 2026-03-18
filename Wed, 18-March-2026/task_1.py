from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()

sleep(2)

checkbox_link = driver.find_element(By.LINK_TEXT, "Checkboxes")
drag_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Drag")
list_items = driver.find_elements(By.TAG_NAME, "li")
print("Total li count:", len(list_items))

sleep(4)
driver.get("https://the-internet.herokuapp.com/tables")
sleep(3)

website = driver.find_element(By.XPATH, "//td[text()='jdoe@hotmail.com']/following-sibling::td[2]")
print("Website:", website.text)

delete_link = driver.find_element(By.XPATH, "//td[text()='Bach']/following-sibling::td/a[text()='delete']")
print("Delete link:", delete_link)

table2 = driver.find_element(By.XPATH, "(//table)[2]")
print("Second table found:", table2)

row = driver.find_element(By.XPATH, "(//table)[2]//td[text()='$100.00']/parent::tr")
print("Row with $100:", row.text)

driver.quit()