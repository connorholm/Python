#Program makes a short summary or topic headlines for the users choosen subject
#Uses webscraping tools BeautifulSoup and request
#Data is collected from Wikipedia
from PIL import Image
from bs4 import BeautifulSoup
import requests
import io

#Creates the summary
#For returnType use an int 0,1,2,3
#0 returns nothing, 1 returns summary, 2 returns the headlines of the subject, 3 returns an image
def parseData(topic, returnType):
    subject = topic
    Headlines = []
    paragraphs = []
    imagelinks = []
    correctImage = 0

    #Gets the website and puts it into a document to be parsed using BeatifulSoup
    url = "https://en.wikipedia.org/wiki/{subject}".format(subject= subject)
    r = requests.get(url)

    #Parsing through the website using BeatifulSoup
    soup = BeautifulSoup(r.text, "html.parser")
    result = soup.find(class_="mw-parser-output")
    narrowed = result.find_all(class_="mw-headline")
    divFinder = soup.find(class_="mw-parser-output")
    pFinderArray = divFinder.find_all("p")
    images = soup.find_all('img')
    for image in images:
        imagelinks.append(image['src'])
    for paragraph in pFinderArray:
        if paragraph.get_text() == "\n":
           continue
        paragraphs.append(paragraph.get_text())
    for texts in narrowed:
        Headlines.append(texts.get_text())

    #Takes the summary containing the "[#]" and removes it from the summary
    jumbledSummary = paragraphs[0]
    summaryIndex = 0
    for character in jumbledSummary:
        if character == "[":
            jumbledSummary = jumbledSummary[0: summaryIndex] + jumbledSummary[summaryIndex+3:]
            summaryIndex-=3
        summaryIndex+=1
    summary = jumbledSummary

    if returnType == 0:
        return ""
    elif returnType == 1:
        return summary
    elif returnType == 2:
        return Headlines
    elif returnType == 3:
        return imagelinks
    

#Creates getter methods
def getHeadlines(topic):
    return parseData(topic, 2)

def getSummary(topic):
    return parseData(topic, 1)
def getImage(topic): 
    return parseData(topic, 3)

#Gets the users desired subject to find summary
def userSubject():
    correctOutputType = False
    output = input("What type of output (summary/headlines/image):")
    subject = input("\nDesired subject: ")
    while correctOutputType == False: 
        if output == "summary":
            return "\n{summary}".format(summary=getSummary(subject))
            correctOutputType = True
        elif output == "headlines":
            return "\n{headlines}".format(headlines=getHeadlines(subject))
            correctOutputType = True
        elif output == "image":
            imagelinks = getImage(subject)
            correctImage = 0
            if (imagelinks[0] == "//upload.wikimedia.org/wikipedia/en/thumb/9/94/Symbol_support_vote.svg/19px-Symbol_support_vote.svg.png") or (imagelinks[0] == "//upload.wikimedia.org/wikipedia/en/thumb/1/1b/Semi-protection-shackle.svg/20px-Semi-protection-shackle.svg.png") or (imagelinks[0] == "//upload.wikimedia.org/wikipedia/commons/thumb/4/47/Sound-icon.svg/20px-Sound-icon.svg.png"):
                correctImage = 1
            if imagelinks[1] == "//upload.wikimedia.org/wikipedia/en/thumb/9/94/Symbol_support_vote.svg/19px-Symbol_support_vote.svg.png" or imagelinks[1] == "//upload.wikimedia.org/wikipedia/en/thumb/1/1b/Semi-protection-shackle.svg/20px-Semi-protection-shackle.svg.png" or imagelinks[1] == "//upload.wikimedia.org/wikipedia/commons/thumb/4/47/Sound-icon.svg/20px-Sound-icon.svg.png":
                correctImage = 2
            if imagelinks[2] == "//upload.wikimedia.org/wikipedia/en/thumb/9/94/Symbol_support_vote.svg/19px-Symbol_support_vote.svg.png" or imagelinks[2] == "//upload.wikimedia.org/wikipedia/en/thumb/1/1b/Semi-protection-shackle.svg/20px-Semi-protection-shackle.svg.png" or imagelinks[2] == "//upload.wikimedia.org/wikipedia/commons/thumb/4/47/Sound-icon.svg/20px-Sound-icon.svg.png":
                correctImage = 3
            response = requests.get("http:"+imagelinks[correctImage])
            image_bytes = io.BytesIO(response.content)
            img = Image.open(image_bytes)
            img.show()
            correctOutputType = True
        else:
            output = input("The desired output type was not recognized\nTry again (summary/headlines/image): ")
    

#Displaying the different headlines
if __name__ == "__main__":
    playAgain = ""
    while playAgain != "x":
        print(userSubject())
        playAgain = input("Tap any key and enter to re-run program (click 'x' and enter to quit): ")
