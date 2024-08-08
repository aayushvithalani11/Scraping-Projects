import pandas as pd
import requests
from bs4 import BeautifulSoup

product_names = []
reviews = []
product_prices = []
descriptions = []

for i in range(2,12):
    url = "https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(1)

    r = requests.get(url)
    #print(r)

    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find("div", class_ = "_1YokD2 _3Mn1Gg")

    names = box.find_all("div", class_ = "_4rR01T")
    for i in names:
        name = i.text
        product_names.append(name)
    print(product_names)

    prices = box.find_all("div", class_ = "_30jeq3 _1_WHN1")
    for i in prices:
        price = i.text
        product_prices.append(price)
    print(product_prices)

    desc = box.find_all("ul", class_ = "_1xgFaf")
    for i in desc:
        name = i.text
        descriptions.append(name)
    print(descriptions)

    rev = box.find_all("div", class_ = "_3LWZlK")
    for i in rev:
        name = i.text
        reviews.append(name)
    print(reviews)


df = pd.DataFrame({"Product_name" : product_names, "Prices" : product_prices, "Descriptions" : descriptions, "Reviews":reviews })
print(df)

df.to_csv("mobiles_under_5000.csv")
