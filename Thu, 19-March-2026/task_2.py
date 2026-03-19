from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from time import sleep


opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

driver.get('https://qavbox.github.io/demo/signup/')
driver.maximize_window()

wait = WebDriverWait(driver, 5)

user_name = wait.until(EC.presence_of_element_located((By.ID, 'username')))
user_name.click()
user_name.send_keys("Tony")

email = wait.until(EC.element_to_be_clickable((By.ID, 'email')))
email.click()
email.send_keys("stark@ironman.com")

phone_no = wait.until(EC.element_to_be_clickable((By.ID, 'tel')))
phone_no.click()
phone_no.send_keys("123456789")

# fax_no = wait.until(EC.element_to_be_clickable((By.ID, 'fax')))
# fax_no.click()
# fax_no.send_keys("123456789")

upload = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='datafile']")))
upload.send_keys(r"C:\Users\jdeve\Downloads\WhatsApp Image 2026-02-18 at 2.06.19 PM.jpeg")

gender_select = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@name='sgender']")))
gender = Select(gender_select)
gender.select_by_value("male")

experience = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//input[@type='radio']")))
experience[3].click()
# for i in experience:
#     if i.get_attribute("value") == "2":
#         i.click()

skills = wait.until(EC.presence_of_all_elements_located((By.ID, 'ip')))
skills[3].click()


tools = wait.until(EC.presence_of_element_located((By.XPATH, "//select[@id='tools']")))
t = Select(tools)

t.select_by_value("Webdriverio")

submit_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='submit']")))
submit_btn.click()

sleep(10)


driver.quit()