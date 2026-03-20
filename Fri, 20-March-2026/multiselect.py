from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

driver.get(r'C:\Users\jdeve\OneDrive\Desktop\Python-Capg\Capgemini_training\playlist.html')
driver.maximize_window()


song_list = driver.find_element(By.ID, 'songs')
select = Select(song_list)

if select.is_multiple:
    select.select_by_index(4)
    select.select_by_visible_text('Shape of You')
    select.select_by_visible_text('Animals')

print([i.text for i in select.all_selected_options])
driver.find_element(By.XPATH, '//button[text()="Add to Playlist"]').click()
sleep(5)
print(select.options)
sleep(5)
driver.quit()