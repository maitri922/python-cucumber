from selenium import webdriver
import time
from selenium.webdriver.common import keys

driver = webdriver.Chrome("C:\\Users\ABC\\PycharmProjects\\pythonproject\\firsttest\\drivers\\chromedriver.exe")
driver.maximize_window()
# driver = webdriver.firefox()
# driver = webdriver.ie()

driver.set_page_load_timeout(10)
driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("what is testing")
time.sleep(10)
driver.find_element_by_name("btnI").click()
time.sleep(4)
driver.quit()
