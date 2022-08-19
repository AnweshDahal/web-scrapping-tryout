from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.daraz.com.np/')

print("Web Page Open")
search_box = driver.find_element("xpath", '//*[@id="q"]')

search_box.send_keys('Fantech GP13 Shooter II')

search_button = driver.find_element("xpath", '//*[@id="topActionHeader"]/div/div[2]/div/div[2]/form/div/div[2]/button')
search_button.click()

# Look if a 
# driver.quit()
