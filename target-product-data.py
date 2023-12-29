import requests
from bs4 import BeautifulSoup
import pandas as pd

# Global Variables
#current_page = 1
url = "https://www.target.com/p/400-thread-count-printed-performance-sheet-set-threshold-153/-/A-14220754"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

productTitle = soup.find("h1", {"id": "pdp-product-title-id"}).text
print(productTitle)
