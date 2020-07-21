from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os, csv
import urllib.request

os.mkdir("images")


NIKE = "https://www.nike.com/kr/ko_kr/"
query = "search?q=티셔츠"

MAX_ITEMS = 40

ID = []
IMAGES = []
PRODUCTS = []
PRICE_TAG = []

user_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}


i = 1
n = 1
page_get = f"&page={i}"

while len(ID) < MAX_ITEMS:
    r = requests.get(NIKE+query+page_get, headers=user_agent)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    item_list = soup.find_all("div", {"class": "a-product"})
    for item in item_list:
        image = item.find("div", {"class": "a-product-image-primary"}).find("img").get("src").strip("?browse")
        title = item.find("p", {"class": "product-display-name"}).text
        price = item.find("p", {"class": "product-display-price"}).text
        ID.append(n)
        PRODUCTS.append(title)
        PRICE_TAG.append(price)
        urllib.request.urlretrieve(image, f"images/{n}.jpg")
        n=n+1
    i = i + 1
    if len(ID) >= MAX_ITEMS:
        break



"""with open('nike.csv', 'w', newline="") as csvfile:
    writer = csv.writer(csvfile)
    for p in ID:
        writer.writerow([ID[p],PRODUCTS[p], PRICE_TAG[p])

"""