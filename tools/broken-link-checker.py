from bs4 import BeautifulSoup, SoupStrainer
import requests

pageUrl = "https://zapier.com"

page = requests.get(pageUrl)
data = page.text
soup = BeautifulSoup(data)

linksArry = []
newArry = []
for hrefs in soup.find_all('a'):
    linksArry.append(hrefs.get('href'))
    for a in linksArry:
        newArry.append(pageUrl+str(a))



url_responses = {}

for link in newArry:
    temp_r = requests.get(link)
    url_responses[link] = temp_r.status_code
