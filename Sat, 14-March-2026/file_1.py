from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

# driver.get("https://www.amazon.in/")
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

sleep(2)

##Ancestor
# ancestor_div = driver.find_element(By.XPATH,"//select[@id='searchDropdownBox']/ancestor::form")
# print("Ancestor element found:", ancestor_div)
# print()
#
# ##Descendant
# descendant_div = driver.find_elements(By.XPATH, "//div[@id='nav-main']/descendant::span[text()='All']")
# print("Descendant element found:",descendant_div)
# print()
#
# ##Parent
# parent_div = driver.find_element(By.XPATH, "//form[@id='nav-search-bar-form']/parent::div")
# print("Parent element:", parent_div)
#
# ##Child
# child_div = driver.find_element(By.XPATH, "//form[@id='nav-search-bar-form']/child::div")
# print("Child element:", child_div)
#
# ##Sibling
# # 1-> Preceding Sibling
# preceding_sibling = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']/preceding::select[@id='searchDropdownBox']")
# print("Preceding element:", preceding_sibling)
#
# # 2-> Followup Sibling


#
# driver.find_element(By.PARTIAL_LINK_TEXT, "Udemy")
# print('i found')




prices = driver.find_elements(By.XPATH, "//table[@name='BookTable']//td[text()='300']")

price_list = []

for p in prices:
    price_list.append(p.text)

print(price_list)


driver.quit()
