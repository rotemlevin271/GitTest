import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys

# 1.
chrome_driver = webdriver.Chrome(service=Service("C:/Users/rotem/Downloads/chromedriver_win32/chromedriver.exe"))
# chrome_driver.get('https://www.walla.co.il')


# firefox_driver = Firefox(service=Service("C:/Users/rotem/Downloads/geckodriver-v0.33.0-win-aarch64/geckodriver.exe"))
# firefox_driver.get('https://www.ynet.co.il')

# 2.  a.
# headLine = chrome_driver.title
# print(headLine)
# b.
# chrome_driver.refresh()
# c.
# haim = chrome_driver.title == headLine
# print(haim)

# 3.
# yes, the element does have the same locators in all the browsers.

# 4.
# chrome_driver.get('https://translate.google.com')
# text_box = chrome_driver.find_element(By.CLASS_NAME, value= 'er8xn').send_keys('רותם המלכה')

# 5.
chrome_driver.get('https://www.youtube.com')
search_box = chrome_driver.find_element(By.ID, value= 'search')
search_box.click()
search_box.send_keys('strangers by nature')
button = chrome_driver.find_element(By.ID, value='search-icon-legacy')
button.click()
# time.sleep(15)
####  לא עבד לי משום מה הכתיבה של הטקסט והחיפוש לא עם עם חיפוש של איידי ולא עם של קלאסניים ##

# 6.

# chrome_driver.get('https://translate.google.com')
# web_element = chrome_driver.find_element(By.XPATH, value="//textarea[@role='combobox' and @rows='1' and @aria-expanded='false']")
# print(web_element)

# 7.
# chrome_driver.get("https://www.facebook.com/")
# chrome_driver.find_element(By.ID, value="email").send_keys("a@a.com")
# chrome_driver.find_element(By.ID, value="pass").send_keys("Aa123")


