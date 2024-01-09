import requests
from bs4 import BeautifulSoup
import pandas as pd

# Global Variables
url = "https://www.target.com/p/400-thread-count-printed-performance-sheet-set-threshold-153/-/A-14220754"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
page = requests.get(url, headers = headers)
soup = BeautifulSoup(page.content, "html.parser")

productTitle = soup.find("h1", {"id": "pdp-product-title-id"}).text
#DPCI = soup.find("b", string="Item Number (DPCI)")

#print(productTitle)
#print(soup.get_text())

#html = soup.prettify("utf-8")

# with open('target.html', "w") as file:
#    file.write(str(soup))