from selenium import webdriver
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)
driver.get("https://www.vlr.gg/")

driver.maximize_window()
sleep(2)
driver.minimize_window()
sleep(2)
driver.maximize_window()
sleep(2)

driver.back()
sleep(2)
driver.forward()
sleep(2)
driver.refresh()
sleep(2)


print(f'Current URL is: {driver.current_url}')
print(f'Driver name: {driver.name}')
print(f'Driver title: {driver.title}')

driver.close()