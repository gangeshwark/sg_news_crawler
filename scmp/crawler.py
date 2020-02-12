# coding:utf-8
# crawl news in SCMP for the page with key word search
import time
from time import sleep

import requests
from bs4 import BeautifulSoup  # 导入bs4库
import re  # 导入正则库

# response = requests.get("http://www.scmp.com/content/search/AAC?f[0]=ds_created%3A%5B2013-01-01T00%3A00%3A00Z%20TO%202016-01-31T23%3A59%3A59Z%5D")
# soup = BeautifulSoup(response.text,'html.parser') #创建beautifulsoup对象
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from tqdm import tqdm
import pandas as pd

data = pd.DataFrame(columns=['headline', 'source_url', 'publish_date', 'publisher'])


def News_dig(website, i=0):
    try:
        response = requests.get(website)
        soup = BeautifulSoup(response.text, 'html.parser')  # 创建beautifulsoup对象

        title = soup.find('h1', {'class': 'info__headline headline'}).get_text()  # 新闻标题
        publish_date = soup.find('meta', {'property': "article:published_time"}).get('content')  # 发布时间
        print(title, publish_date)
        # main_body = soup.find_all(class_="panel-pane pane-entity-field pane-node-body pane-first pos-0")[-1]  # 新闻主体
        # 2020-01-01T16:59:49+08:00
        epoch_time = int(time.mktime(time.strptime(publish_date, '%Y-%m-%dT%H:%M:%S%z')))
        publish_date = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(int(epoch_time)))
        print(publish_date)
        data.loc[i] = [title, website, publish_date, 'SCMP']
        i += 1


    except Exception as e:
        f = open('error.txt', 'a+')
        f.write(website + '\t' + str(e))
        f.close()

    return i


if __name__ == '__main__':
    i = 0
    # News_dig(
    #     'http://www.scmp.com/magazines/style/news-trends/article/3048436/coronavirus-celebrity-donations-fan-bingbing-louis-koo')
    # News_dig(
    #     'http://www.scmp.com/news/hong-kong/health-environment/article/3045444/wuhan-pneumonia-hong-kong-requests-genetic')
    # News_dig('http://www.scmp.com/news/asia')
    # News_dig(
    #     "http://www.scmp.com/news/china/politics/article/3044207/china-shuts-seafood-market-linked-mystery-viral-pneumonia")
    import selenium

    recrawl = False

    if recrawl:
        page_url = 'https://www.scmp.com/topics/coronavirus-outbreak-all-stories'
        # page_url = 'https://academicpages.github.io/'
        print(page_url)
        options = Options()
        options.headless = False
        # browser = webdriver.Firefox(executable_path='../geckodriver', options=options)
        browser = webdriver.Chrome(executable_path='/home/gangeshwark/chromedriver')
        browser.get(page_url)
        browser.maximize_window()
        body_element = browser.find_element_by_tag_name('body')
        # print(body_element.text)
        # print(body_element)
        body_element.click()
        # body_element.send_keys(Keys.CONTROL + Keys.END)

        last_height = browser.execute_script("return document.body.scrollHeight")
        print('last_height', last_height)
        i = 0
        try:
            for x in tqdm(range(120)):
                body_element.send_keys(Keys.CONTROL + Keys.END)
                sleep(1)

        except KeyboardInterrupt as e:
            pass

        content = browser.page_source
        with open("page_source.html", "w") as f:
            f.write(content)
        browser.close()

    scmpnews = BeautifulSoup(open("page_source.html", encoding='UTF-8'), 'html.parser')
    print(len(scmpnews.find_all(href=re.compile("/news/"))))
    all_links = []
    for news_href in scmpnews.find_all(href=re.compile("/news/")):
        l = news_href.get('href')
        if l:
            if l.endswith('.js'):
                continue
            if 'http' in l:
                scmpnews_href = l + '\n'
            else:
                scmpnews_href = 'http://www.scmp.com' + l + '\n'
            all_links.append(scmpnews_href)
        # print(scmpnews)
    all_links = sorted(set(all_links))
    print(len(set(all_links)))
    f = open('all_links.txt', 'w')
    f.writelines(all_links)
    f.close()
    for link in all_links:
        print(link)
        i = News_dig(link.strip(), i)
        data.to_csv('data/all_data.csv', index_label='index')
        data.to_excel('data/all_data.xlsx', index_label='index')
        # News_dig("http://www.scmp.com/news/china/politics/article/3044207/china-shuts-seafood-market-linked-mystery-viral-pneumonia")
