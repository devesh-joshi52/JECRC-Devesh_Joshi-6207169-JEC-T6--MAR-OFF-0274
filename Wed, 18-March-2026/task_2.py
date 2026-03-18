from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

sleep(2)

driver.find_element(By.ID, "firstName").send_keys("Jack")
sleep(1)
driver.find_element(By.ID, "lastName").send_keys("Sparrow")
sleep(1)
driver.find_element(By.ID, "userEmail").send_keys("blackpearl@example.com")
sleep(1)
driver.find_element(By.XPATH, "//label[text()='Male']").click()
sleep(1)
driver.find_element(By.ID, "userNumber").send_keys("9876543210")
sleep(1)
subjects = driver.find_element(By.ID, "subjectsInput")
sleep(1)
subjects.send_keys("Maths")
sleep(1)
driver.find_element(By.XPATH, "//div[text()='Maths']").click()
sleep(1)
driver.find_element(By.XPATH, "//label[text()='Sports']").click()
sleep(1)
driver.find_element(By.ID, "uploadPicture").send_keys(r"C:\Users\jdeve\Downloads\WhatsApp Image 2026-02-18 at 2.06.19 PM.jpeg")
sleep(2)

driver.find_element(By.ID, "currentAddress").send_keys("New Delhi")
sleep(2)

driver.find_element(By.XPATH, '//div[@class = "css-13cymwt-control"]').click()
sleep(1)
driver.find_element(By.XPATH, "//div[text()='NCR']").click()
driver.find_element(By.ID, "city").click()
sleep(1)
driver.find_element(By.XPATH, "//div[text()='Delhi']").click()

sleep(2)

driver.find_element(By.ID, "submit").click()
sleep(2)
print("Form submitted successfully")

sleep(3)
driver.quit()