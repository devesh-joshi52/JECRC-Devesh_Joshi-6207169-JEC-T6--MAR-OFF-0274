from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get("https://www.lenskart.com/")
driver.maximize_window()
sleep(3)

eye = driver.find_element(By.XPATH, '//a[@id="lrd1"]')
# eye = driver.find_element(By.ID, 'lrd1')
print(eye.text)

assert 'GLASSES' in eye.text, 'didnt find'
print('success')

search_bar = driver.find_element(By.ID, 'autocomplete-0-input')
print(search_bar.is_enabled())

eye = driver.find_element(By.ID, 'lrd5').click()
print(eye.text)


# //h4[@class="sc-84016674-0 dbhRRC"]

driver.quit()
