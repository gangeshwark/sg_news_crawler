import requests
from bs4 import BeautifulSoup

url = 'https://www.mothership.sg/2019/12/thai-flight-attendant-quit/'
sourceCode = requests.get(str(url))
soup1 = BeautifulSoup(sourceCode.content, "lxml")
original_article = soup1.find_all('publish-date')
print(original_article)

for s in soup1.find_all('span'):
    if s and s.get('class'):
        if 'publish-date' in s.get('class'):
            pub_date = s.text
            print(pub_date)
    # print(pub_date)

KWs = ['nCov', 'virus', ' Coronavirus', ' Wuhan', '2019-nCoV']
related_article = False
for div in soup1.find_all('div'):
    if div and div.get('class'):
        if 'content-article-wrap' in div.get('class'):
            body_text = div.text
            print(body_text)
            for kw in KWs:
                if kw in body_text:
                    related_article = True
                    print(body_text)
                    break
