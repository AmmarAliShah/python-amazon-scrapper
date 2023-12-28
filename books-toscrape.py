import requests
from bs4 import BeautifulSoup
import pandas as pd

# Global Variables
current_page = 1
proceed = True

while(proceed):
    url = "https://books.toscrape.com/catalogue/page-" + str(current_page)+  ".html"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    
    if soup.title.text == "404 Not Found":
        proceed = False
    else:
        all_books = soup.find_all("article", class_="product_pod")

        for book in all_books:
            item = {}

            item['Title'] = book.find("img").attrs["alt"]
            item['Link'] = book.find()
    current_page += 1