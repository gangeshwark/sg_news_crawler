"""
Script to merge maun
"""
import pandas as pd
import requests
import time
from bs4 import BeautifulSoup
from furl import furl
import re
from datetime import datetime

from jsonschema._utils import indent
from numba.tests.test_array_exprs import ax2

manual_data_path = 'manual_data/'


def cna():
    pass


def st():
    pass


def toz():
    pass


def nyt():
    pass


def scmp():
    pass


def mothership():
    pass


def guardian():
    pass


def remove_params(urls):
    n_urls = []
    for url in urls:
        url = furl(url).remove(args=True, fragment=True).url
        # print(url)
        n_urls.append(url)
    return n_urls


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
        i += 1

    except Exception as e:
        f = open('error.txt', 'a+')
        f.write(website + '\t' + str(e) + '\n')
        f.close()

    return i


def today_():
    auto_data = pd.read_csv('today/data/all_data.csv', index_col='index')
    manual_data = pd.read_csv(manual_data_path + 'today.csv')
    print(auto_data.columns)
    manual_data.columns = auto_data.columns
    print(manual_data.columns)
    print(auto_data.shape)
    print(manual_data.shape)

    manual_url = manual_data['source_url'].values
    auto_url = auto_data['source_url'].values
    manual_url = remove_params(manual_url)
    manual_data['source_url'] = manual_url

    new_data = auto_data.append(manual_data)
    print(new_data.shape)
    new_data.drop_duplicates(['source_url'], inplace=True)
    print(new_data.shape)
    # print(new_data.iloc[330:])
    da = new_data.iloc[330:]
    print(da.shape, type(da))

    def format_date(date):
        d = datetime.strptime(date, '%d %B, %Y').strftime('%d-%m-%Y')
        return d

    for i, d in enumerate(da.iterrows()):
        print(d[1]['source_url'])
        new_data.iloc[i + 330] = [d[1]['headline'].strip(), d[1]['source_url'], format_date(d[1]['publish_date']),
                                  d[1]['publisher']]

    new_data.reset_index(inplace=True)
    new_data.drop(['index'], axis=1, inplace=True)
    new_data.to_csv('merged_data/today.csv', index_label='index')
    new_data.to_excel('merged_data/today.xlsx', index_label='index')


if __name__ == '__main__':
    today_()
