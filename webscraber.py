import requests
from bs4 import BeautifulSoup


url = 'https://www.codewithtomi.com'
r = requests.get(url)
print(r)


soup = BeautifulSoup(r.content, 'lxml')
title = soup.find_all('h2', {'class':'post-title'})
print(title)
title1 = title[0].getText()
print(title1)


for t in title:
    print(t.getText())