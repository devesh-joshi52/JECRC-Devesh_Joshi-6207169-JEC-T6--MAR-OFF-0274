#To open Chrome browser
from selenium import webdriver
from time import sleep


# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(options=opts)


# sleep(5)
# driver = webdriver.Edge()
# sleep(5)

opts = webdriver.FirefoxOptions()
opts.set_preference('detach', True)
driver = webdriver.Firefox(options=opts)
# sleep(5)

driver.get("https://supertails.com/")
driver.maximize_window()
sleep(2)

# driver.minimize_window()
# sleep(2)


# driver.back()
# sleep(2)
# driver.forward()
# sleep(2)
# driver.refresh()
# sleep(2)
print(f'Current URL is: {driver.current_url}')
print(f'Driver name: {driver.name}')
print(f'Driver title: {driver.title}')

# driver.close()
driver.quit()

