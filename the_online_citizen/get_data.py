import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_data_bs(url):
    sourceCode = requests.get(str(url))
    soup1 = BeautifulSoup(sourceCode.content, "lxml")
    # original_article = soup1.find('article original')

    headline = soup1.find('h1').text
    pub_date = ''
    # print(soup1.find_all('span'))
    pub_dates = []
    for s in soup1.find_all('span'):
        if s and s.get('class'):
            if 'elementor-icon-list-text' in s.get('class'):
                pub_dates.append(s.text)

    print(pub_dates)
    pub_date = pub_dates[1][8:].strip()
    print(headline)
    print(pub_date)

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
    for i, url in enumerate(urls):
        print(url.strip())
        url = url.strip()
        headline, publish_date = get_data_bs(url)
        if headline:
            data.loc[i] = [headline, url, publish_date, 'The Online Citizen']
            # data = data.append([headline, url, publish_date, 'Mothership'])
        data.to_csv('data/all_data.csv', index_label='index')
        data.to_excel('data/all_data.xlsx', index_label='index')
        # exit()
