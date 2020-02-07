from bs4 import BeautifulSoup, SoupStrainer
from assertpy import assert_that
import requests

pageUrl = "http://the-internet.herokuapp.com/login"

page = requests.get(pageUrl)
data = page.text
soup = BeautifulSoup(data, 'html.parser')

linksArry = []
newArry = []

for hrefs in soup.find_all('a'):
    linksArry.append(hrefs.get('href'))
    for a in linksArry:
        newArry.append(str(a))

for link in newArry:
    temp_r = requests.get(link)
    assert_that(temp_r.status_code).is_equal_to(200)
