import time

import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm


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
    if pub_date == '':
        f = open('data/error.txt')
        f.write(url)
        f.close()
        return False, False
    # February 12, 11:20 pm
    try:
        epoch_time = int(time.mktime(time.strptime('2020 ' + pub_date, '%Y %B %d, %I:%M %p')))
        pub_date = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(int(epoch_time + (8 * 60 * 60))))
    except Exception as e:
        f = open('data/error.txt')
        f.write(url + '\t' + str(e))
        f.close()

    # print(headline)
    # print(pub_date)

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
    with open('data/all_urls_new.txt', 'r') as URLS:
        urls = URLS.readlines()

    data = pd.DataFrame(columns=['headline', 'source_url', 'publish_date', 'publisher'])
    i = 0
    for url in tqdm(urls):
        # print(url.strip())
        url = url.strip()
        headline, publish_date = get_dat_bs(url)
        if headline:
            data.loc[i] = [headline, url, publish_date, 'Mothership']
            i += 1
            # data = data.append([headline, url, publish_date, 'Mothership'])
        data.to_csv('data/all_data_new.csv', index_label='index')
        data.to_excel('data/all_data_new.xlsx', index_label='index')
