#Main goal is to learn more about webscraping using BeautifulSoup and Request

from bs4 import BeautifulSoup
import requests

Headline = []

#Gets the website and puts it into a document to be parsed using BeatifulSoup
url = "https://en.wikipedia.org/wiki/Bill Gates"
r = requests.get(url)

#Parsing through the website using BeatifulSoup
soup = BeautifulSoup(r.text, "html.parser")
result = soup.find(class_="mw-parser-output")
narrowed = result.find_all(class_="mw-headline")
for texts in narrowed:
    Headline.append(texts.get_text())

#Displaying the different headlines
print(Headline)
