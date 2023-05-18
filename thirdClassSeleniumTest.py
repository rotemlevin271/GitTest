import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service("C:/Users/rotem/Downloads/chromedriver_win32/chromedriver.exe"))
driver.implicitly_wait(10)
driver.get('https://translate.google.com')
but = driver.find_element(By.CLASS_NAME, value='ySES5')
my_list = driver.find_elements(By.TAG_NAME, value='ySES5')
print(len(my_list))
but.click()

text_box = driver.find_element(By.CLASS_NAME, value= 'er8xn').send_keys('kapunkap')
text_box = driver.find_element(By.CLASS_NAME, value= 'er8xn').send_keys(Keys.END) #כמו לחיצה על כפתור הEND במקלדת, יורד לסוף העמוד 
driver.find_element(By.CLASS_NAME, value= 'er8xn').clear()
time.sleep(10)
print(driver.current_url)
print(driver.title)
driver.quit()
