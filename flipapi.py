from bs4 import BeautifulSoup
import requests


def getFlippers():
    site = requests.get("https://ship.flipp.dev/")
    soup = BeautifulSoup(site.text, features="html.parser")
    shipped = soup.find_all(class_="flipper")[0]
    textfilter = filter(str.isdigit, shipped)
    shipped = "".join(textfilter)
    gotten = soup.find_all(class_="flipper")[1]
    textfilter = filter(str.isdigit, gotten)
    gotten = "".join(textfilter)
    result = f"{shipped} {gotten}"
    return result
