from bs4 import BeautifulSoup
import requests
import pytest

pageUrl = "http://the-internet.herokuapp.com/login"

page = requests.get(pageUrl)
data = page.text
soup = BeautifulSoup(data, "html.parser")

linksArry = []
newArry = []

def test_links_on_page():
    for hrefs in soup.find_all("a"):
        linksArry.append(hrefs.get("href"))
        for a in linksArry:
            newArry.append(str(a))

    for link in newArry:
        temp_r = requests.get(link)
        assert temp_r.status_code == 200
