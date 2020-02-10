import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_dat_bs(url):
    sourceCode = requests.get(str(url))
    soup1 = BeautifulSoup(sourceCode.content, "lxml")
    # original_article = soup1.find('article original')

    headline = soup1.find('h1').text
    pub_date = ''
    # print(soup1.find_all('span'))
    for s in soup1.find_all('span'):
        if s and s.get('class'):
            if 'publish-date' in s.get('class'):
                pub_date = s.text
                break
    print(headline)
    print(pub_date)

    # check if the article is related to corona virus
    KWs = ['nCov', 'virus', 'Virus', 'coronavirus', 'Coronavirus', 'wuhan', 'Wuhan', '2019-nCoV']
    related_article = False
    for div in soup1.find_all('div'):
        if div and div.get('class'):
            if 'content-article-wrap' in div.get('class'):
                body_text = div.text
                # print(body_text)
                for kw in KWs:
                    # kw = kw.lower()
                    if kw in headline:
                        related_article = True
                        break
                    if kw in body_text:
                        related_article = True
                        break
    if related_article:
        return headline, pub_date
    else:
        return False, False


if __name__ == '__main__':
    with open('all_urls.txt', 'r') as URLS:
        urls = URLS.readlines()

    data = pd.DataFrame(columns=['headline', 'source_url', 'publish_date', 'publisher'])
    for i, url in enumerate(urls):
        print(url.strip())
        url = url.strip()
        headline, publish_date = get_dat_bs(url)
        if headline:
            data.loc[i] = [headline, url, publish_date, 'Mothership']
            # data = data.append([headline, url, publish_date, 'Mothership'])
        data.to_csv('all_data.csv', index_label='index')
        data.to_excel('all_data.xlsx', index_label='index')
