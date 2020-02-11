import time
from datetime import datetime

import pandas as pd
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from tqdm import tqdm

from db_setup import NewsArticle, db
import uuid


def get_data(main_urls):
    count = 0
    for main_url in tqdm(main_urls):
        print(main_url)
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(executable_path='../geckodriver',
                                    options=options)

        browser.get(main_url)
        content = browser.page_source

        # sourceCode = requests.get(str(main_url))
        soup1 = BeautifulSoup(content, "lxml")
        # print(soup1)
        f = open('test.html', 'w')
        f.write(str(content))
        # time.sleep(10)

        a_time = soup1.find_all('time')
        a_head = soup1.find_all('h3')
        print('a_head', a_head)
        _t = 0
        for i, h in enumerate(a_head):
            print(i)
            if 'teaser__heading' in h.get('class'):
                t = a_time[_t]
                _t += 1
                link = h.find('a')
                url = 'https://www.channelnewsasia.com' + link.get('href')
                headline = link.text
                ep_time = t.get('datetime')
                # get time in tz
                # tz = pytz.timezone('Asia/Singapore')
                dt = datetime.fromtimestamp(int(ep_time))
                # print it

                publish_time = time.strftime('%Y-%m-%d ', time.localtime(int(ep_time)))

                print(headline)
                print(url)
                print(publish_time)
                # print(publish_time2)
                data.loc[count] = [headline, url, publish_time, 'Channel News Asia']
                news_article = NewsArticle()
                news_article.id = uuid.uuid3(uuid.NAMESPACE_URL, url)
                news_article.headline = headline
                news_article.URL = url
                news_article.publish_time = publish_time
                news_article.source_name = 'Channel News Asia'
                news_article.save()

                # NewsArticle.create(
                #     id=uuid.uuid3(uuid.NAMESPACE_URL, url),
                #     headline=headline,
                #     URL=url,
                #     publish_time=publish_time,
                #     source_name='Channel News Asia',
                # )
                count += 1
        data.to_csv('data/all_data1.csv', index_label='index')
        data.to_excel('data/all_data1.xlsx', index_label='index')
        browser.close()
        # exit()


if __name__ == '__main__':
    print(db.connect())
    main_urls = ['https://www.channelnewsasia.com/news/topic/coronavirus']
    for i in range(1, 2):
        url = "https://www.channelnewsasia.com/news/topic/coronavirus?pageNum={0}".format(i)
        main_urls.append(url)

    print(main_urls)
    data = pd.DataFrame(columns=['headline', 'source_url', 'publish_date', 'publisher'])
    # get_data('https://www.channelnewsasia.com/news/topic/coronavirus?pageNum=2')
    # exit()

    get_data(main_urls)
    db.close()
