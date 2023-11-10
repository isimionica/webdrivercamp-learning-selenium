from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
driver = webdriver.Chrome()
driver.get("http://www.ebay.com")
print(driver.title)

search = driver.find_element(By.ID, 'gh-ac')
search.send_keys("women watch")
search.send_keys(Keys.RETURN)

time.sleep(5)
driver.close()






