from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

path = "H:\All\Selenium\chromedriver.exe"
s = Service(path)
driver = webdriver.Chrome(service=s)
driver.get("https://www.google.com/")
time.sleep(1)

box = driver.find_element(By.CSS_SELECTOR, "textarea[class='gLFyf']").send_keys("House of dragon", Keys.ENTER)
driver.find_element(By.CSS_SELECTOR, "a[href='https://www.hbo.com/house-of-the-dragon'").click()
driver.save_screenshot("H:\All\PycharmProjects\Selenium - House Of Dragons\dragon.png")

