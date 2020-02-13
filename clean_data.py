"""
Script to merge maun
"""
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
    # print(manual_url)
    # print(auto_url)
    # print(len(set(manual_url)))
    # print(len(set(auto_url)))
    # print(len(set(auto_url) & set(manual_url)))
    # print(auto_data[~auto_data.isin(manual_data)].dropna())
    # common = auto_data.merge(manual_data, on=['source_url'])
    # print(common.columns)
    # new = auto_data[(~auto_data.source_url.isin(common.source_url))&(~auto_data.source_url.isin(common.source_url))]
    # print(new.shape)
    # print(new.columns)

    new_data = auto_data.append(manual_data)
    print(new_data.shape)
    new_data.drop_duplicates(['source_url'], inplace=True)
    print(new_data.shape)
    new_data.to_csv('merged_data/today.csv')


if __name__ == '__main__':
    today_()
