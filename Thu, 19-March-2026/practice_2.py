from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

driver.get('https://demo.mobiscroll.com/select/multiple-select')
driver.maximize_window()

multi_drop = driver.find_element(By.XPATH, '//seect[@id="multiple-select-select"]')
select = Select(multi_drop)

if select.is_multiple():
    select.select_by_value('1')
    select.select_by_value('2')
    select.select_by_value('3')
