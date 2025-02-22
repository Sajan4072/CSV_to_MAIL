import re
from selenium import webdriver

#initialize chorme driver
# chrome_driver='path'
# driver - webdriver.Chrome(chrome_driver)

# or

driver = webdriver.Chrome()
#qty 50
driver.get('https://www.randomlists.com/email-addresses?qty=50')

driver.close()