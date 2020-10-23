from bs4 import BeautifulSoup
import requests

def getProductList():
    url = "https://minneapolis.craigslist.org/search/sss?sort=rel&max_price=0"
    page = requests.get(url)

    soup = BeautifulSoup(page.text, "html.parser")
    #User puts in a word, program returns items of the word that are free
    print(soup)

if __name__ == "__main__":
    getProductList()