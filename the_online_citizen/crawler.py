from bs4 import BeautifulSoup

html = open('data/news.html', 'r')
content = html.read()
soup1 = BeautifulSoup(content, "lxml")
# print(soup1)

articles = soup1.find_all('article')
print(len(articles))
_num = 0
all_urls = []
for article in articles:
    divs = article.find_all('div')
    for div in divs:
        if 'jeg_postblock_content' in div.get('class'):
            for a in div.find_all("a"):
                if "theonlinecitizen.com" in a.get("href"):
                    print(a.get("href"))
                    all_urls.append(a.get("href"))
                    _num += 1
                    break
print(_num)

with open('data/all_urls.txt', 'w+') as URLS:
    for url in all_urls:
        URLS.write(url + '\n')
        # get_data(url)
