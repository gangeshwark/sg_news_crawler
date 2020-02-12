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
                if _t >= 10:
                    break
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

                publish_time = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(int(ep_time)))

                print(headline)
                print(url)
                print(publish_time)
                # print(publish_time2)
                data.loc[count] = [headline, url, publish_time, 'Channel News Asia']
                count += 1
        data.to_csv('data/all_data_new.csv', index_label='index')
        data.to_excel('data/all_data_new.xlsx', index_label='index')
        browser.close()
        # exit()


if __name__ == '__main__':
    main_urls = ['https://www.channelnewsasia.com/archives/12301794/wuhan-virus?&channelId=12301828']
    for i in range(1, 78):
        url = "https://www.channelnewsasia.com/archives/12301794/wuhan-virus?pageNum={0}&channelId=12301828".format(i)
        main_urls.append(url)

    print(main_urls)
    data = pd.DataFrame(columns=['headline', 'source_url', 'publish_date', 'publisher'])
    # get_data('https://www.channelnewsasia.com/news/topic/coronavirus?pageNum=2')
    # exit()

    get_data(main_urls)
