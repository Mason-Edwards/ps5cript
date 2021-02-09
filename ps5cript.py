import requests
import time
from bs4 import BeautifulSoup

URL = "https://www.argos.co.uk/vp/oos/ps5.html?clickSR=slp:term:playstation%205:1:565:1"

while(True):
    time.sleep(1)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find(id="h1title")

    #print(result)

    if result != None and "Sorry, PlayStation®5 is currently unavailable." in result:
        print("PS5 is unavaliable")
    else:
       print("PS5 Is avaliable")

