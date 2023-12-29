import requests
from bs4 import BeautifulSoup
import pandas as pd

# Global Variables
#current_page = 1
url = "https://www.amazon.com/Queen-Piece-Sheet-Set-Breathable/dp/B089XSMCFN"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

productTitle = soup.find("span", {"id": "productTitle"}).text
print(productTitle)



# while(proceed):
#     print("Currently on page " + str(current_page))

#     page = requests.get(url)
#     soup = BeautifulSoup(page.text, "html.parser")
    
#     if soup.title.text == "404 Not Found":
#         proceed = False
#     else:
#         all_books = soup.find_all("article", class_="product_pod")

#         for book in all_books:
#             item = {}

#             item['Title'] = book.find("img").attrs["alt"]
#             item['Link'] = book.find("a").attrs["href"]
#             item['Price'] = book.find("p", class_="price_color").text[1:]
#             item['Stock'] = book.find("p", class_="instock availability").text.strip()

#             data.append(item);

#     current_page += 1

# df = pd.DataFrame(data)
# df.to_excel("books.xlsx")