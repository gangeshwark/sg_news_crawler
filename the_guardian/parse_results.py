import json
import time
from os import walk
from pprint import pprint
import pandas as pd
from tqdm import tqdm

if __name__ == '__main__':

    mypath = '/projects/PycharmProjects/sg_news_crawler/the_guardian/data/all_articles/'
    import glob

    data = pd.DataFrame(columns=['headline', 'source_url', 'publish_date', 'publisher'])
    # pprint(sorted(glob.glob(mypath + "*.json")))
    i = 0
    for f_path in tqdm(sorted(glob.glob(mypath + "*.json"))):
        fp = open(f_path, 'r')
        articles = json.load(fp)
        print(len(articles))
        for article in articles:
            headline = article['webTitle']
            url = article['webUrl']
            publish_time = article['webPublicationDate']
            # 2019-12-20T23:40:45Z
            epoch_time = int(time.mktime(time.strptime(publish_time, '%Y-%m-%dT%H:%M:%S%z')))
            publish_time = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(int(epoch_time + (8 * 60 * 60))))
            source_name = 'The Guardian'
            body_text = article['fields']['body']
            # print(body_text)

            # check if the article is related to corona virus
            check = True
            if check:
                KWs = ['nCov', 'coronavirus', 'Coronavirus', 'wuhan', 'Wuhan', '2019-nCoV']
                related_article = False
                # print(body_text)
                for kw in KWs:
                    # kw = kw.lower(
                    if kw in headline:
                        related_article = True
                        break
                    if kw in body_text:
                        related_article = True
                        if kw in ['virus', 'Virus']:
                            if 'Ebola' in body_text:
                                related_article = False
                                continue
                        break
                if related_article:
                    data.loc[i] = [headline, url, publish_time, source_name]
                    i += 1
            else:
                data.loc[i] = [headline, url, publish_time, source_name]
                i += 1

        data.to_csv('data/all_data.csv', index_label='index')
        data.to_excel('data/all_data.xlsx', index_label='index')
