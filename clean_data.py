"""
Script to merge maun
"""
import time
from datetime import datetime

import pandas as pd
from furl import furl

manual_data_path = 'manual_data/'


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


def cna():
    auto_data = pd.read_csv('cna/data/all_data_new.csv', index_col='index')
    manual_data = pd.read_csv(manual_data_path + 'cna.csv')
    auto_data['crawl_type'] = 'auto'
    manual_data['crawl_type'] = 'manual'
    manual_data.columns = auto_data.columns

    def reformat_url(url):
        url = remove_param(url)
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

    # exit()

    def format_date(date):
        try:
            # 05 Feb 2020 5:00 PM
            d = datetime.strptime(date, '%d %b %Y %H:%M %p').strftime('%d/%m/%Y %H:%M')
        except:
            # 31-01-2020 02:28:19
            epoch_time = int(time.mktime(time.strptime(date, '%d-%m-%Y %H:%M:%S')))
            d = time.strftime('%d/%m/%Y %H:%M', time.localtime(int(epoch_time)))
        return d

    for i, d in enumerate(new_data.iterrows()):
        # print(d[1]['source_url'])
        new_data.iloc[i] = [d[1]['headline'].strip(), remove_param(d[1]['source_url']),
                            format_date(d[1]['publish_date']), 'Channel News Asia', d[1]['crawl_type']]

    new_data.drop_duplicates(['source_url'], inplace=True)
    # Sort by date

    new_data['Date'] = pd.to_datetime(new_data.publish_date, format='%d/%m/%Y %H:%M')
    new_data = new_data.sort_values('Date', ascending=True)
    new_data.reset_index(inplace=True)
    new_data.drop(['index', 'Date'], axis=1, inplace=True)
    new_data.to_csv('merged_data/cna.csv', index_label='index')
    new_data.to_excel('merged_data/cna.xlsx', index_label='index')
    return new_data


def st():
    auto_data = pd.read_csv('the_strait_times/data/all_data_new.csv', index_col='index')
    manual_data = pd.read_csv(manual_data_path + 'straits_times.csv')
    auto_data['crawl_type'] = 'auto'
    manual_data['crawl_type'] = 'manual'
    manual_data.columns = auto_data.columns

    def reformat_url(url):
        url = remove_param(url)
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

    # exit()

    def format_date(date):
        date = date.strip()
        try:
            # JAN 2, 2020, 9:01 PM
            d = datetime.strptime(date, '%b %d, %Y, %H:%M %p').strftime('%d/%m/%Y %H:%M')
        except:
            # 13-02-2020 03:28:43
            epoch_time = int(time.mktime(time.strptime(date, '%d-%m-%Y %H:%M:%S')))
            d = time.strftime('%d/%m/%Y %H:%M', time.localtime(int(epoch_time)))
        return d

    for i, d in enumerate(new_data.iterrows()):
        # print(d[1]['source_url'])
        new_data.iloc[i] = [d[1]['headline'].strip(), remove_param(d[1]['source_url']),
                            format_date(d[1]['publish_date']), 'The Straits Times', d[1]['crawl_type']]

    new_data.drop_duplicates(['source_url'], inplace=True)
    print(new_data.shape)
    # Sort by date
    new_data['Date'] = pd.to_datetime(new_data.publish_date, format='%d/%m/%Y %H:%M')
    new_data = new_data.sort_values('Date', ascending=True)
    new_data.reset_index(inplace=True)
    new_data.drop(['index', 'Date'], axis=1, inplace=True)
    new_data.to_csv('merged_data/the_strait_times.csv', index_label='index')
    new_data.to_excel('merged_data/the_strait_times.xlsx', index_label='index')
    return new_data


def toc():
    auto_data = pd.read_csv('the_online_citizen/data/all_data_new.csv', index_col='index')
    manual_data = pd.read_csv(manual_data_path + 'the_online_citizen.csv')
    auto_data['crawl_type'] = 'auto'
    manual_data['crawl_type'] = 'manual'
    manual_data.columns = auto_data.columns

    def reformat_url(url):
        url = remove_param(url)
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

    # exit()

    def format_date(date):
        try:
            # 05 Feb 2020 5:00 PM
            d = datetime.strptime(date, '%d %b %Y %H:%M %p').strftime('%d/%m/%Y %H:%M')
        except:
            # 31-01-2020 02:28:19
            epoch_time = int(time.mktime(time.strptime(date, '%d-%m-%Y %H:%M:%S')))
            d = time.strftime('%d/%m/%Y %H:%M:%S', time.localtime(int(epoch_time)))
        return d

    for i, d in enumerate(new_data.iterrows()):
        # print(d[1]['source_url'])
        new_data.iloc[i] = [d[1]['headline'].strip(), remove_param(d[1]['source_url']),
                            format_date(d[1]['publish_date']), 'The Online Citizen', d[1]['crawl_type']]

    new_data.drop_duplicates(['source_url'], inplace=True)
    # Sort by date
    new_data['Date'] = pd.to_datetime(new_data.publish_date, format='%d/%m/%Y %H:%M:%S')
    new_data = new_data.sort_values('Date', ascending=True)
    new_data.reset_index(inplace=True)
    new_data.drop(['index', 'Date'], axis=1, inplace=True)
    new_data.to_csv('merged_data/the_online_citizen.csv', index_label='index')
    new_data.to_excel('merged_data/the_online_citizen.xlsx', index_label='index')
    return new_data


def nyt():
    auto_data = pd.read_csv('nyt/data/all_data.csv', index_col='index')
    manual_data = pd.read_csv(manual_data_path + 'nyt.csv')
    auto_data['crawl_type'] = 'auto'
    manual_data['crawl_type'] = 'manual'
    manual_data.columns = auto_data.columns

    manual_url = manual_data['source_url'].values
    auto_url = auto_data['source_url'].values
    manual_url = remove_params(manual_url)
    manual_data['source_url'] = manual_url

    def reformat_url(url):
        url = remove_param(url)
        return url

    # manual_data['source_url'] = manual_data['source_url'].apply(lambda x: reformat_url(x))
    # auto_data['source_url'] = auto_data['source_url'].apply(lambda x: reformat_url(x))
    print(auto_data.shape)
    print(manual_data.shape)
    new_data = auto_data
    print(new_data.shape)
    new_data.drop_duplicates(['source_url'], inplace=True)
    print(new_data.shape)
    sh1 = auto_data.shape[0]
    print(sh1)
    auto_data.to_csv('merged_data/nyt.csv', index_label='index')
    new_data.to_excel('merged_data/nyt.xlsx', index_label='index')

    da = new_data.iloc[sh1:]
    print(da.shape, type(da))

    # exit()

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
                            format_date(d[1]['publish_date']), 'The New York Times', d[1]['crawl_type']]

    new_data.drop_duplicates(['source_url'], inplace=True)
    # Sort by date

    new_data['Date'] = pd.to_datetime(new_data.publish_date, format='%d/%m/%Y %H:%M:%S')
    new_data = new_data.sort_values('Date', ascending=True)
    new_data.reset_index(inplace=True)
    new_data.drop(['index', 'Date'], axis=1, inplace=True)
    new_data.to_csv('merged_data/nyt.csv', index_label='index')
    new_data.to_excel('merged_data/nyt.xlsx', index_label='index')
    return new_data


def scmp():
    auto_data = pd.read_csv('scmp/data/all_data.csv', index_col='index')
    manual_data = pd.read_csv(manual_data_path + 'scmp.csv')
    auto_data['crawl_type'] = 'auto'
    manual_data['crawl_type'] = 'manual'
    manual_data.columns = auto_data.columns

    def reformat_url(url):
        url = remove_param(url)
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
                            format_date(d[1]['publish_date']), 'SCMP', d[1]['crawl_type']]

    new_data.drop_duplicates(['source_url'], inplace=True)
    # Sort by date

    new_data['Date'] = pd.to_datetime(new_data.publish_date, format='%d/%m/%Y %H:%M:%S')
    new_data = new_data.sort_values('Date', ascending=True)
    new_data.reset_index(inplace=True)
    new_data.drop(['index', 'Date'], axis=1, inplace=True)
    new_data.to_csv('merged_data/scmp.csv', index_label='index')
    new_data.to_excel('merged_data/scmp.xlsx', index_label='index')
    return new_data


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
                            format_date(d[1]['publish_date']), 'Mothership.sg', d[1]['crawl_type']]

    new_data.drop_duplicates(['source_url'], inplace=True)
    # Sort by date

    new_data['Date'] = pd.to_datetime(new_data.publish_date, format='%d/%m/%Y %H:%M')
    new_data = new_data.sort_values('Date', ascending=True)
    new_data.reset_index(inplace=True)
    new_data.drop(['index', 'Date'], axis=1, inplace=True)
    new_data.to_csv('merged_data/mothership.csv', index_label='index')
    new_data.to_excel('merged_data/mothership.xlsx', index_label='index')
    return new_data


def guardian():
    """No data yet"""
    auto_data = pd.read_csv(manual_data_path + 'guardian_auto.csv', index_col='Index')
    manual_data = pd.read_csv(manual_data_path + 'guardian.csv')
    manual_data.columns = ['headline', 'source_url', 'publish_date', 'publisher']
    auto_data.columns = ['headline', 'source_url', 'publish_date', 'publisher']
    auto_data['crawl_type'] = 'auto'
    manual_data['crawl_type'] = 'manual'

    def reformat_url(url):
        url = remove_param(url)
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

    # exit()

    def format_date(date):
        try:
            # 05 Jan 2020 2:25 PM
            d = datetime.strptime(date, '%d %b %Y %H:%M%p').strftime('%d/%m/%Y %H:%M')
        except:
            # 07-01-2020 14:34:32
            epoch_time = int(time.mktime(time.strptime(date, '%d-%m-%Y %H:%M:%S')))
            d = time.strftime('%d/%m/%Y %H:%M', time.localtime(int(epoch_time)))
        return d

    for i, d in enumerate(new_data.iterrows()):
        # print(d[1]['source_url'])
        new_data.iloc[i] = [d[1]['headline'].strip(), remove_param(d[1]['source_url']),
                            format_date(d[1]['publish_date']), 'The Guardian', d[1]['crawl_type']]

    new_data.drop_duplicates(['source_url'], inplace=True)
    # Sort by date
    new_data['Date'] = pd.to_datetime(new_data.publish_date, format='%d/%m/%Y %H:%M')
    new_data = new_data.sort_values('Date', ascending=True)
    new_data.reset_index(inplace=True)
    new_data.drop(['index', 'Date'], axis=1, inplace=True)
    new_data.to_csv('merged_data/the_guardian.csv', index_label='index')
    new_data.to_excel('merged_data/the_guardian.xlsx', index_label='index')
    return new_data


def independent_sg():
    """No data yet"""
    manual_data = pd.read_csv(manual_data_path + 'independent_sg.csv', index_col='Index')
    manual_data.columns = ['headline', 'source_url', 'publish_date', 'publisher']
    manual_data['crawl_type'] = 'manual'

    print(manual_data.shape)
    new_data = manual_data
    print(new_data.shape)
    new_data.drop_duplicates(['source_url'], inplace=True)
    print(new_data.shape)

    for i, d in enumerate(new_data.iterrows()):
        # print(d[1]['source_url'])
        new_data.iloc[i] = [d[1]['headline'].strip(), remove_param(d[1]['source_url']),
                            d[1]['publish_date'], 'The Independent Singapore', d[1]['crawl_type']]

    new_data.drop_duplicates(['source_url'], inplace=True)
    # Sort by date

    new_data['Date'] = pd.to_datetime(new_data.publish_date, format='%d/%m/%Y')
    new_data = new_data.sort_values('Date', ascending=True)
    new_data.reset_index(inplace=True)
    new_data.drop(['Index', 'Date'], axis=1, inplace=True)
    new_data.to_csv('merged_data/independent_sg.csv', index_label='index')
    new_data.to_excel('merged_data/independent_sg.xlsx', index_label='index')
    return new_data


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
                            'Today Online', d[1]['crawl_type']]

    # Sort by date
    new_data['Date'] = pd.to_datetime(new_data.publish_date, format='%d/%m/%y')
    new_data = new_data.sort_values('Date', ascending=True)
    new_data.reset_index(inplace=True)
    new_data.drop(['index', 'Date'], axis=1, inplace=True)
    new_data.to_csv('merged_data/today.csv', index_label='index')
    new_data.to_excel('merged_data/today.xlsx', index_label='index')
    return new_data


if __name__ == '__main__':
    today_data = today_()
    mothership_data = mothership()
    scmp_data = scmp()
    nyt_data = nyt()
    cna_data = cna()
    toc_data = toc()
    st_data = st()
    ind_data = independent_sg()
    guard_data = guardian()

    new_data = today_data.append(
        [mothership_data, scmp_data, nyt_data, cna_data, toc_data, st_data, ind_data, guard_data])

    new_data.reset_index(inplace=True)
    new_data.drop(['index'], axis=1, inplace=True)
    new_data.to_csv('merged_data/headlines_data_full.csv', index_label='index')
    new_data.to_excel('merged_data/headlines_data_full.xlsx', index_label='index')
