from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome()
driver.get("https://abc.com")
driver.maximize_window()


# driver.implicitly_wait(5)
# driver.find_element(By.ID, "firstName").send_keys("Jack")
# driver.implicitly_wait(5)
# driver.find_element(By.ID, "lastName").send_keys("Sparrow")


wait_obj = WebDriverWait(driver, 10, poll_frequency=200)

submit_button = wait_obj.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='submit']")))
submit_button.click()

driver.quit()