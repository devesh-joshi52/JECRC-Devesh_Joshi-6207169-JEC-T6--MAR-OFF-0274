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

song_list = driver.find_element(By.ID, "songs")
select = Select(song_list)

# options = driver.find_elements(By.XPATH, "//optgroup[@label='Twenty One Pilots']/option")
#
# if select.is_multiple:
#     for opt in options:
#         select.select_by_visible_text(opt.text)
#
# print([i.text for i in select.all_selected_options])



options = song_list.find_elements(By.XPATH, "//optgroup[@label='One Direction']/option")

if select.is_multiple:
    for opt in options:
        opt.click()

print([i.text for i in select.all_selected_options])

driver.find_element(By.XPATH, '//button[text()="Add to Playlist"]').click()
sleep(5)

driver.quit()