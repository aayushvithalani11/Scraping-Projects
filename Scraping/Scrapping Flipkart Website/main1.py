import requests
from bs4 import BeautifulSoup
import mysql.connector

# Connect to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Sunny0411@@kobe",
  database="test"
)

mycursor = mydb.cursor()

# Create a table to store the scraped data
mycursor.execute("CREATE TABLE products (name VARCHAR(255), price VARCHAR(255), description TEXT, review VARCHAR(255))")

# Scrape the data
product_names = []
reviews = []
product_prices = []
descriptions = []

for i in range(2,12):
    url = "https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(1)

    r = requests.get(url)

    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find("div", class_ = "_1YokD2 _3Mn1Gg")

    names = box.find_all("div", class_ = "_4rR01T")
    for i in names:
        name = i.text
        product_names.append(name)

    prices = box.find_all("div", class_ = "_30jeq3 _1_WHN1")
    for i in prices:
        price = i.text
        product_prices.append(price)

    desc = box.find_all("ul", class_ = "_1xgFaf")
    for i in desc:
        name = i.text
        descriptions.append(name)

    rev = box.find_all("div", class_ = "_3LWZlK")
    for i in rev:
        name = i.text
        reviews.append(name)

# Insert the scraped data into the table
for i in range(len(product_names)):
    sql = "INSERT INTO products (name, price, description, review) VALUES (%s, %s, %s, %s)"
    val = (product_names[i], product_prices[i], descriptions[i], reviews[i])
    mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) inserted.")
