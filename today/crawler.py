'https://www.todayonline.com/topics/coronavirus'
import re
import time
from time import sleep

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from tqdm import tqdm
import pandas as pd

data = pd.DataFrame(columns=['headline', 'source_url', 'publish_date', 'publisher'])


def News_dig(website, i=0):
    try:
        response = requests.get(website)
        soup = BeautifulSoup(response.text, 'html.parser')  # 创建beautifulsoup对象

        title = soup.find('title').get_text()  # 新闻标题
        body = soup.find('body')
        publish_date = body.find('script').get_text()  # 发布时间
        publish_date = re.findall(r"\D(\d{8})\D", publish_date)[-1]
        print(publish_date)
        print(title, publish_date)
        # main_body = soup.find_all(class_="panel-pane pane-entity-field pane-node-body pane-first pos-0")[-1]  # 新闻主体
        # 2020-01-01T16:59:49+08:00
        # epoch_time = int(time.mktime(time.strptime(publish_date, '%Y%m%d')))
        # publish_date = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(int(epoch_time)))
        publish_date = publish_date[6:] + '-' + publish_date[4:6] + '-' + publish_date[:4]
        print(publish_date)
        data.loc[i] = [title, website, publish_date, 'Today Online']
        i += 1

    except Exception as e:
        f = open('error.txt', 'a+')
        f.write(website + '\t' + str(e) + '\n')
        f.close()

    return i


if __name__ == '__main__':

    i = 0

    recrawl = False

    if recrawl:
        page_url = 'https://www.todayonline.com/topics/coronavirus'
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
        # body_element.click()
        # body_element.send_keys(Keys.CONTROL + Keys.END)

        last_height = browser.execute_script("return document.body.scrollHeight")
        print('last_height', last_height)
        i = 0
        try:
            for x in tqdm(range(200)):
                body_element.send_keys(Keys.CONTROL + Keys.END)
                sleep(2)

        except KeyboardInterrupt as e:
            pass

        content = browser.page_source
        with open("page_source.html", "w") as f:
            f.write(content)
        browser.close()

    today_news = BeautifulSoup(open("page_source.html", encoding='UTF-8'), 'html.parser')
    all_data = today_news.find_all('li', {'class': 'col-md-12'})
    print(len(all_data))
    # exit()
    all_links = []
    for news_cont in all_data:
        a = news_cont.find('a')

        l = a.get('href')
        # print(l)
        # exit()
        if l:
            if l.endswith('.js'):
                continue
            if 'http' in l:
                scmpnews_href = l + '\n'
            else:
                scmpnews_href = 'https://www.todayonline.com' + l + '\n'
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
