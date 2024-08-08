from bs4 import BeautifulSoup
import requests
import selenium
from selenium.webdriver.common.by import By

url = "https://books.toscrape.com/catalogue/category/books/philosophy_7/index.html"

def proxy_request(url):
    payload = {
        "source": "universal",
        "url": url,
        "geo_location": "Germany"
    }
    response = requests.request(
        "POST": "https://realtime.oxylabs.io/v1/queries",
        auth = "",
        json = payload
    )
    response_html = response.json()['results'][0]['content']
    return BeautifulSoup(response_html,"lxml")

soup = proxy_request(url)
prices = soup.find_all(By.CSS_SELECTOR, "p[class_='price_color']")
price_list = [price.text[1:] for price in prices]
print(statistics.mean(price_list))
