from bs4 import BeautifulSoup
import requests
import statistics
import selenium
from selenium.webdriver.common.by import By

url = "https://books.toscrape.com/catalogue/category/books/philosophy_7/index.html"

r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
prices = soup.find_all(By.CSS_SELECTOR, "p[class_='price_color']")
price_list = [price.text[1:] for price in prices]
print(statistics.mean(price_list))