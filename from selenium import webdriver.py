from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#point to where your web driver is
service = Service(executable_path='chromedriver.exe')
#initialize driver
driver = webdriver.Chrome(service=service)

#navigate to webpage
driver.get('https://google.com')

#tell the driver to wwait x seconds or until a specific element loads
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'gLFyf')))

#finds a specific element of a webpage (use dev tools to find what you need in the browser)
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
#clears an input field
input_element.clear()
#types and interacts with input field
input_element.send_keys('Dota 2' + Keys.ENTER)

WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Dota 2' )))

#find an element by partial text
link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Dota 2')
#click on a link
link.click()

time.sleep(10)

driver.quit()