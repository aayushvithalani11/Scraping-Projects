import requests
from bs4 import BeautifulSoup

url = ("https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets")
r = requests.get(url)
#print(r)

soup = BeautifulSoup(r.text, "lxml")
#print(soup.prettify())

#boxes = soup.findAll("div", class_="col-sm-4 col-lg-4 col-md-4")

names = soup.findAll("a", class_="title")
for i in names:
    print(i.text)

prices = soup.findAll("h4", class_="pull-right price")
for i in prices:
    print(i.text)