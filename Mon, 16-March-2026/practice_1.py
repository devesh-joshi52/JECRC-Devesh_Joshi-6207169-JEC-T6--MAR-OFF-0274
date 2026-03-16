# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from time import sleep
#
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(options=opts)
#
# websites = [
#     "https://www.amazon.in/",
#     "https://www.nike.com/",
#     "https://www.bbc.com/",
#     "https://www.lenskart.com/"
# ]
#
# for site in websites:
#     driver.get(site)
#     # driver.maximize_window()
#     # sleep(2)
#     # search_field = driver.find_element(By.ID, 'twotabsearchtextbox')
#     #
#     # search_field.clear()
#     # search_field.send_keys("Headphones", Keys.ENTER)
#     # sleep(2)
#     sleep(3)
#     print("Page Title:", driver.title)
#
# driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from time import sleep
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get("https://www.amazon.in/")
# driver.maximize_window()
# sleep(2)
# search_field = driver.find_element(By.ID, 'twotabsearchtextbox')
#
# search_field.clear()
# search_field.send_keys("Headphones", Keys.ENTER)
# sleep(2)
#
#
#
# driver.quit()

