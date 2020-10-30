from bs4 import BeautifulSoup
import requests

def getProductList():
    url = "https://minneapolis.craigslist.org/search/sss?sort=rel&max_price=0"
    page = requests.get(url)

    soup = BeautifulSoup(page.text, "html.parser")
    #User puts in a word, program returns items of the word that are free
    titlesHTML = soup.find_all(class_ = "result-heading")
    titles = []
    correctTitle = ""
    titleLength = 0
    for title in titlesHTML:
        correctTitle = title.get_text()
        titles.append(correctTitle[1:len(correctTitle)-1:])
    print(titles)

if __name__ == "__main__":
    getProductList()
