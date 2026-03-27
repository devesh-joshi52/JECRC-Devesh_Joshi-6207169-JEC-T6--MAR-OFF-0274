# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from time import sleep
#
# # Complete Flow On Amazon
# # Steps:
# # Open website
# # Verify homepage title & URL
# # Search for product → "Headphones"
# # Apply filters (Brand,price(upto 500 or above 1000 anything))
# # Open a product → switch to new tab
# # Verify product details (title, price) using assert
# # Add to cart
# # Go to cart verify item (using assert with the name used eailer)
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# wait = WebDriverWait(driver, 15)
#
# driver.get("https://www.amazon.in/")
#
# # assert "Amazon" in driver.title
# assert "amazon.in" in driver.current_url
# sleep(2)
# search = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
# sleep(2)
# search.send_keys("Headphones", Keys.ENTER)
# sleep(2)
# # wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'₹500 - ₹1,000')]"))).click()
# # sleep(2)
# # wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'boAt')]"))).click()
# # sleep(2)
# # product = wait.until(EC.element_to_be_clickable((By.XPATH, "(//h2//a)[1]")))
# wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'₹500 - ₹1,000')]"))).click()
# wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'boAt')]"))).click()
#
# wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-component-type='s-search-result']")))
#
# wait.until(EC.presence_of_element_located((By.TAG_NAME, "h2")))
#
# products = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//h2/a")))
#
# product = products[0]
# product_name = product.text
#
# driver.execute_script("arguments[0].click();", product)
# product.click()
# sleep(2)
# driver.switch_to.window(driver.window_handles[1])
# sleep(2)
# title = wait.until(EC.presence_of_element_located((By.ID, "productTitle"))).text
# sleep(2)
# price = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='a-price-whole'])[1]"))).text
#
# assert product_name.split()[0] in title
# assert price != ""
#
# wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-button"))).click()
# wait.until(EC.element_to_be_clickable((By.ID, "nav-cart"))).click()
#
# cart_item = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='a-truncate-cut']"))).text
#
# assert product_name.split()[0] in cart_item
#
# print("Flow completed successfully")


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 15)

driver.get("https://www.amazon.in/")

assert "amazon.in" in driver.current_url

search = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
search.send_keys("Headphones", Keys.ENTER)

wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-component-type='s-search-result']")))

wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'₹600 - ₹1,100')]"))).click()
wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-component-type='s-search-result']")))

wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'boAt')]"))).click()
wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-component-type='s-search-result']")))

products = wait.until(EC.presence_of_all_elements_located(
    (By.XPATH, "//div[@data-component-type='s-search-result']//h2/a")
))

product = products[0]
product_name = product.text

driver.execute_script("arguments[0].click();", product)

wait.until(lambda d: len(d.window_handles) > 1)
driver.switch_to.window(driver.window_handles[1])

title = wait.until(EC.presence_of_element_located((By.ID, "productTitle"))).text
price = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='a-price-whole'])[1]"))).text

assert product_name.split()[0] in title
assert price != ""

wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-button"))).click()
wait.until(EC.element_to_be_clickable((By.ID, "nav-cart"))).click()

cart_item = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='a-truncate-cut']"))).text

assert product_name.split()[0] in cart_item

print("Flow completed successfully")