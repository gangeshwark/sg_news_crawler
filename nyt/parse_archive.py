import json
import time
from datetime import datetime

import pandas as pd
from tqdm import tqdm


def get_docs():
    data = pd.DataFrame(columns=['headline', 'source_url', 'publish_date', 'publisher'])

    j_file_1 = open('archive_1_2020.json', 'r')
    j_file_2 = open('archive_2_2020.json', 'r')
    docs_1 = json.load(j_file_1)['response']
    docs_2 = json.load(j_file_2)['response']
    print(docs_1.keys())
    all_docs = docs_1['docs'] + docs_2['docs']
    i = 0
    # dict_keys(['abstract', 'web_url', 'snippet', 'lead_paragraph', 'print_section', 'print_page', 'source', 'multimedia', 'headline', 'keywords', 'pub_date', 'document_type', 'news_desk', 'section_name', 'byline', 'type_of_material', '_id', 'word_count', 'uri'])
    for docs in tqdm(all_docs):
        # print(all_docs[0].keys())
        # print(all_docs[0]['headline'])
        # print(all_docs[0]['keywords'])
        # print(all_docs[0]['pub_date'])
        # print(all_docs[0]['web_url'])
        # print()
        source_name = 'The New York Times'
        headline = docs['headline']['main']
        publish_date = docs['pub_date']
        # 2020-02-11T05:54:15+0000
        # '%b %d, %Y, %I:%M %p'
        epoch_time = int(time.mktime(time.strptime(publish_date, '%Y-%m-%dT%H:%M:%S%z')))
        publish_date = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(int(epoch_time + (8 * 60 * 60))))
        # .strftime('%Y-%m-%d ')

        url = docs['web_url']
        abstract = docs['abstract']
        snippet = docs['snippet']
        lead_paragraph = docs['lead_paragraph']
        keywords = docs['keywords']

        # check if the article is related to corona virus
        check = True
        if check:
            KWs = ['nCov', 'coronavirus', 'Coronavirus', 'wuhan', 'Wuhan', '2019-nCoV', 'pneumonia', 'Pneumonia']
            related_article = False
            # print(body_text)
            for kw in KWs:
                # kw = kw.lower(
                if kw in headline:
                    related_article = True
                    break
                if kw in snippet:
                    related_article = True
                    break
                if kw in abstract:
                    related_article = True
                    if kw in ['virus', 'Virus']:
                        if 'Ebola' in abstract:
                            related_article = False
                            continue
                    break
                if kw in lead_paragraph:
                    related_article = True
                    if kw in ['virus', 'Virus']:
                        if 'Ebola' in lead_paragraph:
                            related_article = False
                            continue
                    break
            if related_article:
                data.loc[i] = [headline, url, publish_date, source_name]
                i += 1
        else:
            data.loc[i] = [headline, url, publish_date, source_name]
            i += 1

        # headline = docs['headline']

        # data.loc[i] = [headline, url, publish_date, 'The New York Times']
        # i += 1
    print(data.shape)
    data.drop_duplicates(inplace=True, keep='first')
    urls = data['source_url']
    print(data.shape)
    print(len(urls))
    print(len(set(urls)))
    data = data.reset_index(drop=True)
    data.to_csv('data/all_data.csv', index_label='index')
    data.to_excel('data/all_data.xlsx', index_label='index')


if __name__ == '__main__':
    get_docs()
