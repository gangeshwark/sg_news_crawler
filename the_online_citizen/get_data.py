import time

import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm


def get_data_bs(url):
    sourceCode = requests.get(str(url))
    soup1 = BeautifulSoup(sourceCode.content, "lxml")
    # original_article = soup1.find('article original')

    headline = soup1.find('h1').text
    pub_date = ''
    # print(soup1.find_all('span'))
    publish_dates = soup1.find('meta', {'property': 'article:published_time'})
    # print(publish_dates.get('content'))

    pub_date = publish_dates.get('content')
    # print(headline)
    # 2020-02-10T07:58:10+00:00
    # print(pub_date)
    epoch_time = int(time.mktime(time.strptime(pub_date[:-6], '%Y-%m-%dT%H:%M:%S')))
    pub_date = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(int(epoch_time + (8 * 60 * 60))))
    # print(pub_date)

    # check if the article is related to corona virus
    related_article = False
    KWs = ['nCov', 'virus', 'Virus', 'coronavirus', 'Coronavirus', 'wuhan', 'Wuhan', '2019-nCoV']
    body_text = ''
    for p in soup1.find_all('p'):
        body_text += (p.text + '\n')
    # body_text = div.text
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
    with open('data/all_urls.txt', 'r') as URLS:
        urls = URLS.readlines()

    data = pd.DataFrame(columns=['headline', 'source_url', 'publish_date', 'publisher'])
    i = 0
    for url in tqdm(urls):
        # print(url.strip())
        url = url.strip()
        headline, publish_date = get_data_bs(url)
        if headline:
            # print([headline, url, publish_date, 'The Online Citizen'])
            data.loc[i] = [headline, url, publish_date, 'The Online Citizen']
            i += 1
        data.to_csv('data/all_data_new.csv', index_label='index')
        data.to_excel('data/all_data_new.xlsx', index_label='index')
