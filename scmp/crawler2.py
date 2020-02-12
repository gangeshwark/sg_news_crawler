# coding:utf-8
# crawl news in SCMP for the page with key word search
from time import sleep

import requests
from bs4 import BeautifulSoup  # 导入bs4库
import re
import pandas as pd

# response = requests.get("http://www.scmp.com/content/search/AAC?f[0]=ds_created%3A%5B2013-01-01T00%3A00%3A00Z%20TO%202016-01-31T23%3A59%3A59Z%5D")
# soup = BeautifulSoup(response.text,'html.parser') #创建beautifulsoup对象
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from tqdm import tqdm

i = 0

data = pd.DataFrame(columns=['headline', 'source_url', 'publish_date', 'publisher'])


def News_dig(website):
    response = requests.get(website)
    soup = BeautifulSoup(response.text, 'html.parser')  # 创建beautifulsoup对象

    title = soup.find('h1').get_text()  # 新闻标题
    published_date = soup.find('meta', {'property': "article:published_time"}).get('content')  # 发布时间
    # updated_date = soup.find_all(class_="node-updated")  # 更新时间
    print(title, published_date)
    data.loc[i] = [title, website, published_date, 'SCMP']
    data.to_csv('data/all_data.csv', index_label='index')
    data.to_excel('data/all_data.xlsx', index_label='index')

    # main_body = soup.find_all(class_="panel-pane pane-entity-field pane-node-body pane-first pos-0")[-1]  # 新闻主体


for j in tqdm(range(0, 200)):

    pagesite = "http://www.scmp.com/search/iphone?page=" + str(
        j) + "&f[0]=ds_created%3A%5B2019-12-25T00%3A00%3A00Z%20TO%202020-02-11T23%3A59%3A59Z%5D"
    print(pagesite)
    newspage = requests.get(pagesite)  # 取搜索页面的html

    pagesoup = BeautifulSoup(newspage.text, 'html.parser')  # 创建beautifulsoup对象

    search_result = pagesoup.find_all(
        class_=re.compile("search-result article"))  # 抓取主页中search-result article split的内容并保存成html文件
    # print(search_result)
    f = open('scmpnews.html', 'w', encoding='utf-8')
    f.writelines(str(search_result))
    f.close()

    scmpnews = BeautifulSoup(open("scmpnews.html", encoding='UTF-8'), 'html.parser')

    for news_href in scmpnews.find_all(href=re.compile("/news")):
        scmpnews_href = 'http://www.scmp.com' + news_href.get('href')
        print(scmpnews_href)
        # print (type(news_href))

        News_dig(scmpnews_href)
        i += 1
