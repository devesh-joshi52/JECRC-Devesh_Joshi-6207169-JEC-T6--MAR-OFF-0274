# TAsk 3
# 1. navigate to amazon
# 2. search a product through send_keys
# BUT dont click on search or keys.enter
# 3. Wait for the suggestions to appear
# 4. Click on 4th suggestion
# 5. Click on Sort By and click on newest
# 6. Click on free shipping check box
# 7. wait for first product and return me the name=price
# (without using inner text)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from time import sleep


opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)


driver.get("https://www.amazon.in/")
driver.maximize_window()

wait = WebDriverWait(driver, 5)


search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
search_box.send_keys("laptop")

suggestions = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@role='row'])[4]")))
suggestions.click()

sort_dropdown = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='a-dropdown-prompt']")))
sort_dropdown.click()

select_dropdown = wait.until(EC.presence_of_element_located((By.XPATH, "(//ul[@class='a-nostyle a-list-link']/child::li)[5]")))
select_dropdown.click()

free_shipping = wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@class='a-icon a-icon-checkbox'])[1]")))
free_shipping.click()

product_name = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='a-section a-spacing-small a-spacing-top-small']/descendant::span")))
name = product_name.text

product_price = wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@data-component-type='s-search-result'])[1]//span[@class='a-price-whole']")))
price = product_price.text

print(f"{name} = ₹{price}")

driver.quit()