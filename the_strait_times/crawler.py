import time
from datetime import datetime

import pandas as pd
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from tqdm import tqdm


def format_time(str_time):
    import time
    epoch_time = int(time.time())
    if 'min' in str_time:
        substract = [int(s) for s in str_time.split() if s.isdigit()]
        substract = substract[0] * 60
        epoch_time -= substract
        time = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(int(epoch_time)))

    elif 'hour' in str_time:
        substract = [int(s) for s in str_time.split() if s.isdigit()]
        substract = substract[0] * 60 * 60
        epoch_time -= substract
        time = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(int(epoch_time)))
    else:
        time = datetime.strptime(str_time, '%b %d, %Y, %I:%M %p').strftime('%d-%m-%Y %H:%M:%S')

    return time


def get_data(main_url):
    count = 1
    for x in range(0, 147):
        page_url = main_url.format(x)
        print(page_url)
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(executable_path='../geckodriver',
                                    options=options)

        browser.get(page_url)
        content = browser.page_source

        # sourceCode = requests.get(str(page_url))
        # content = sourceCode.content
        soup = BeautifulSoup(content, "lxml")
        # print(content)
        # time.sleep(10)

        a_headlines = soup.find_all('span', {'class': 'story-headline'})
        a_time = soup.find_all('div', {'class': 'node-postdate'})
        # print(a_time)
        # assert len(a_time) == 10

        # print(a_headlines)
        lines = [span.get_text().strip() for span in a_headlines]
        pub_times = [format_time(span.get_text().strip()) for span in a_time]
        urls = [span.find('a').get('href').strip() for span in a_headlines]
        print('lines', lines)
        print('urls', urls)
        print('times', pub_times)
        for headline, url, publish_time in zip(lines, urls, pub_times):
            data.loc[count] = [headline, url, publish_time, 'The Straits Times']
            count += 1
        browser.close()
        data.to_csv('data/all_data_new.csv', index_label='index')
        data.to_excel('data/all_data_new.xlsx', index_label='index')


if __name__ == '__main__':
    data = pd.DataFrame(columns=['headline', 'source_url', 'publish_date', 'publisher'])
    main_url = 'https://www.straitstimes.com/tags/coronavirus?page={0}'
    get_data(main_url)
