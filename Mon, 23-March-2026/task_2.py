from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.myntra.com/?utm_source=dms_google&utm_medium=dms_searchbrand_cpc&utm_campaign=dms_google_searchbrand_cpc_Search_Brand_Myntra_Brand_India_BM_TROAS_SOK_New&gad_source=1&gad_campaignid=20443628324&gbraid=0AAAAADoxBh6WcqQi1RuHLiYRHokRt3wFu&gclid=CjwKCAjwyYPOBhBxEiwAgpT8P6tNbrwN4LatytkWx7WHDTeXeEiKyy-Jmded8M1l95IgWdnfncdBaBoCdAMQAvD_BwE")
driver.maximize_window()
action = ActionChains(driver)

wait = WebDriverWait(driver, 10)

gender = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@data-group='women']")))
action.move_to_element(gender).perform()

category = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Shrugs']")))
category.click()
sleep(3)

for i in range(0,5):
    action.send_keys(Keys.PAGE_DOWN).perform()
    sleep(1)

sleep(5)

driver.quit()





