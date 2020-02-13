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
    auto_data = pd.read_csv('mothership/data/all_data_new.csv', index_col='index')
    manual_data = pd.read_csv(manual_data_path + 'mothership.csv')
    manual_data.columns = auto_data.columns

    print(auto_data.shape)
    print(manual_data.shape)
    new_data = auto_data.append(manual_data)
    print(new_data.shape)
    new_data.drop_duplicates(['source_url'], inplace=True)
    print(new_data.shape)
    sh1 = auto_data.shape[0]
    print(sh1)

    da = new_data.iloc[sh1:]
    print(da.shape, type(da))

    def format_date(date):
        try:
            d = datetime.strptime('2020 ' + date, '%Y %B %d, %I:%M %p').strftime('%d-%m-%Y %H:%M')
        except:
            d = datetime.strptime(date, '%d %b %Y %I:%M %p').strftime('%d-%m-%Y %H:%M')
        return d

    for i, d in enumerate(da.iterrows()):
        print(d[1]['source_url'])
        new_data.iloc[i + 330] = [d[1]['headline'].strip(), remove_param(d[1]['source_url']),
                                  format_date(d[1]['publish_date']),
                                  d[1]['publisher']]

    new_data.reset_index(inplace=True)
    new_data.drop(['index'], axis=1, inplace=True)
    new_data.to_csv('merged_data/mothership.csv', index_label='index')
    new_data.to_excel('merged_data/mothership.xlsx', index_label='index')


def guardian():
    pass


def remove_params(urls):
    n_urls = []
    for url in urls:
        url = remove_param(url)
        # print(url)
        n_urls.append(url)
    return n_urls


def remove_param(url):
    return furl(url).remove(args=True, fragment=True).url


def split_date_time():
    pass


def today_():
    auto_data = pd.read_csv('today/data/all_data.csv', index_col='index')
    auto_data['crawl_type'] = 'auto'
    manual_data = pd.read_csv(manual_data_path + 'today.csv')
    manual_data['crawl_type'] = 'manual'
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
        try:
            d = datetime.strptime(date, '%d %B, %Y').strftime('%Y-%d-%m')
        except:
            d = datetime.strptime(date, '%d-%m-%Y').strftime('%Y-%d-%m')
        return d

    for i, d in enumerate(new_data.iterrows()):
        print(d[1]['source_url'])
        new_data.iloc[i] = [d[1]['headline'].strip(), d[1]['source_url'], format_date(d[1]['publish_date']),
                            d[1]['publisher'], d[1]['indicator']]
    new_data['Date'] = pd.to_datetime(new_data.publish_date, format='%Y-%d-%m')
    new_data = new_data.sort_values('Date', ascending=True)
    new_data.reset_index(inplace=True)
    new_data.drop(['index'], axis=1, inplace=True)
    new_data.to_csv('merged_data/today.csv', index_label='index')
    new_data.to_excel('merged_data/today.xlsx', index_label='index')


if __name__ == '__main__':
    today_()
    # mothership()
