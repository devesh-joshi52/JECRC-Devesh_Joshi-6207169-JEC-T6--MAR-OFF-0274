from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)


driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()


id1 = driver.find_element(By.ID, "name")
print("1->ID found:", id1)

id2 = driver.find_element(By.ID, "autocomplete")
print("2->ID found:", id2)

id3 = driver.find_element(By.ID, "alertbtn")
print("3->ID found:", id3)

id4 = driver.find_element(By.ID, "confirmbtn")
print("4->ID found:", id4)

id5 = driver.find_element(By.ID, "openwindow")
print("5->ID found:", id5)



name1 = driver.find_element(By.NAME, "enter-name")
print("1->Name found:", name1)

name2 = driver.find_element(By.NAME, "radioButton")
print("2->Name found:", name2)

name3 = driver.find_element(By.NAME, "show-hide")
print("3->Name found:", name3)

name4 = driver.find_element(By.NAME, "enter-name")
print("4->Name found:", name4)

name5 = driver.find_element(By.NAME, "dropdown-class-example")
print("5->Name found:", name5)



class1 = driver.find_element(By.CLASS_NAME, "inputs")
print("1->Class found:", class1)

class2 = driver.find_element(By.CLASS_NAME, "radioButton")
print("2->Class found:", class2)

class3 = driver.find_element(By.CLASS_NAME, "btn-style")
print("3->Class found:", class3)

class4 = driver.find_element(By.CLASS_NAME, "block")
print("4->Class found:", class4)

class5 = driver.find_element(By.CLASS_NAME, "table-display")
print("5->Class found:", class5)



driver.quit()