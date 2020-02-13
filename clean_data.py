"""
Script to merge maun
"""
import time
from datetime import datetime

import pandas as pd
from furl import furl

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
    auto_data = pd.read_csv('scmp/data/all_data.csv', index_col='index')
    manual_data = pd.read_csv(manual_data_path + 'scmp.csv')
    auto_data['crawl_type'] = 'auto'
    manual_data['crawl_type'] = 'manual'
    manual_data.columns = auto_data.columns

    def reformat_url(url):
        if 'http://' in url:
            url = 'https' + url[4:]
        elif 'https://' in url:
            pass
        return url

    manual_data['source_url'] = manual_data['source_url'].apply(lambda x: reformat_url(x))
    auto_data['source_url'] = auto_data['source_url'].apply(lambda x: reformat_url(x))
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
    new_data.to_csv('merged_data/scmp.csv', index_label='index')

    def format_date(date):
        try:
            # 10-02-2020 12:00:20
            d = datetime.strptime(date, '%d-%m-%Y %H:%M:%S').strftime('%d/%m/%Y %H:%M:%S')
        except:
            # 2020-01-07T22:34:12+08:00
            epoch_time = int(time.mktime(time.strptime(date[:-6], '%Y-%m-%dT%H:%M:%S')))
            d = time.strftime('%d/%m/%Y %H:%M:%S', time.localtime(int(epoch_time)))
        return d

    for i, d in enumerate(new_data.iterrows()):
        # print(d[1]['source_url'])
        new_data.iloc[i] = [d[1]['headline'].strip(), remove_param(d[1]['source_url']),
                            format_date(d[1]['publish_date']), d[1]['publisher'], d[1]['crawl_type']]

    new_data.drop_duplicates(['source_url'], inplace=True)
    # Sort by date

    new_data['Date'] = pd.to_datetime(new_data.publish_date, format='%d/%m/%Y %H:%M:%S')
    new_data = new_data.sort_values('Date', ascending=True)
    new_data.reset_index(inplace=True)
    new_data.drop(['index', 'Date'], axis=1, inplace=True)
    new_data.to_csv('merged_data/scmp.csv', index_label='index')
    new_data.to_excel('merged_data/scmp.xlsx', index_label='index')


def mothership():
    auto_data = pd.read_csv('mothership/data/all_data_new.csv', index_col='index')
    manual_data = pd.read_csv(manual_data_path + 'mothership.csv')
    auto_data['crawl_type'] = 'auto'
    manual_data['crawl_type'] = 'manual'
    manual_data.columns = auto_data.columns

    def reformat_url(url):
        u = url.split('//')
        url = u[0] + '//www.' + u[1]
        return url

    manual_data['source_url'] = manual_data['source_url'].apply(lambda x: reformat_url(x))

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
            d = datetime.strptime('2020 ' + date, '%Y %B %d, %I:%M %p').strftime('%d/%m/%Y %H:%M')
        except:
            try:
                d = datetime.strptime(date, '%d %b %Y %I:%M %p').strftime('%d/%m/%Y %H:%M')
            except:
                d = datetime.strptime(date, '%d-%m-%Y %H:%M:%S').strftime('%d/%m/%Y %H:%M')
        return d

    for i, d in enumerate(new_data.iterrows()):
        # print(d[1]['source_url'])
        new_data.iloc[i] = [d[1]['headline'].strip(), remove_param(d[1]['source_url']),
                            format_date(d[1]['publish_date']), d[1]['publisher'], d[1]['crawl_type']]

    new_data.drop_duplicates(['source_url'], inplace=True)
    # Sort by date

    new_data['Date'] = pd.to_datetime(new_data.publish_date, format='%d/%m/%Y %H:%M')
    new_data = new_data.sort_values('Date', ascending=True)
    new_data.reset_index(inplace=True)
    new_data.drop(['index', 'Date'], axis=1, inplace=True)
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
    manual_data = pd.read_csv(manual_data_path + 'today.csv')
    auto_data['crawl_type'] = 'auto'
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
            d = datetime.strptime(date, '%d %B, %Y').strftime('%d/%m/%y')
        except:
            d = datetime.strptime(date, '%d-%m-%Y').strftime('%d/%m/%y')
        return d

    for i, d in enumerate(new_data.iterrows()):
        # print(d[1]['source_url'])
        new_data.iloc[i] = [d[1]['headline'].strip(), d[1]['source_url'], format_date(d[1]['publish_date']),
                            d[1]['publisher'], d[1]['crawl_type']]

    # Sort by date
    new_data['Date'] = pd.to_datetime(new_data.publish_date, format='%d/%m/%y')
    new_data = new_data.sort_values('Date', ascending=True)
    new_data.reset_index(inplace=True)
    new_data.drop(['index', 'Date'], axis=1, inplace=True)
    new_data.to_csv('merged_data/today.csv', index_label='index')
    new_data.to_excel('merged_data/today.xlsx', index_label='index')


if __name__ == '__main__':
    # today_()
    # mothership()
    scmp()
