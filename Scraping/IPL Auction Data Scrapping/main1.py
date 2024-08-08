import mysql.connector
import requests
from bs4 import BeautifulSoup

# Make a connection to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sunny0411@@kobe",
    database="new"
)

cursor = conn.cursor()

url = "https://www.iplt20.com/auction/2022"
r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")

table = soup.find("table", class_="ih-td-tab auction-tbl")
title = table.find_all("th")
names = []
for i in title:
     name = i.text
     names.append(name)

rows = table.find_all("tr")
for i in rows[1:]:
    first_data = i.find_all("td")[0].find("div", class_= "ih-pt-ic").text.strip()
    data = i.find_all("td")[1:]
    row = [tr.text for tr in data]
    row.insert(0, first_data)
    print("Row length:", len(row))
    print("Row contents:", row)
    cursor.execute(
        "INSERT INTO ipl_auction_stats (Player_Name, Team_Name, Base_Price, Final_Price, Role) VALUES (%s, %s, %s, %s, %s)",
        (row[0], row[1], row[2], row[3], row[4]))

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
