from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os, csv
import urllib.request


def scrape(keyword, value):
    os.mkdir("images")
    NIKE = "https://www.nike.com/kr/ko_kr/"
    query = f"search?q={keyword}"

    MIN_ITEMS = value

    ID = []
    PRODUCTS = []
    PRICE_TAG = []
    INVALID_URL = {
        "id":[],
        "url":[]
    }

    user_agent = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }

    
    os.mkdir("images")
    i = 1 #page_num
    n = 1 #id
    page_get = f"&page={i}"

    while len(ID) < MIN_ITEMS:
        r = requests.get(NIKE+query+page_get, headers=user_agent)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        item_list = soup.find_all("div", {"class": "a-product"})
        for item in item_list:
            image = item.find("div", {"class": "a-product-image-primary"}).find("img").get("src").strip("?browse").strip("")
            title = item.find("p", {"class": "product-display-name"}).text
            price = item.find("p", {"class": "product-display-price"}).text
            ID.append(n)
            PRODUCTS.append(title)
            PRICE_TAG.append(price)
            try:
                urllib.request.urlretrieve(image, f"images/{n}.jpg")
            except Exception:
                INVALID_URL['id'].append(n)
                INVALID_URL['url'].append(image)
            n=n+1
        i = i + 1
        if len(ID) >= MIN_ITEMS:
            break

    with open('invalid_url.txt', 'w') as file:
        for t in range(0,len(INVALID_URL['id'])):
            file.write(f"{INVALID_URL['id'][t]}.jpg: {INVALID_URL['url']}\n")

    with open('nike.csv', 'w', newline="") as csvfile:
        writer = csv.writer(csvfile)
        for num in ID:
            writer.writerow([num,PRODUCTS[num-1], PRICE_TAG[num-1]])
    return
