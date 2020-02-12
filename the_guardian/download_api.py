import json
import requests
from os import makedirs
from os.path import join, exists
from datetime import date, timedelta

ARTICLES_DIR = join('data', 'coronovirus_outbreak_articles_new')
makedirs(ARTICLES_DIR, exist_ok=True)
# exit()
# Sample URL
#
# http://content.guardianapis.com/search?from-date=2016-01-02&
# to-date=2016-01-02&order-by=newest&show-fields=all&page-size=200
# &api-key=your-api-key-goes-here

MY_API_KEY = open("cred2.txt").read().strip()
API_ENDPOINT = 'http://content.guardianapis.com/search'
my_params = {
    # 'q': "coronovirus OR wuhan OR virus OR pneumonia",
    # 'q': " ",
    # 'section': 'world',
    # 'tag': "world/coronovirus-outbreak",
    # 'tag': "world/world",
    'from-date': "",
    'to-date': "",
    'order-by': "newest",
    'show-fields': 'all',
    'page-size': 200,
    'api-key': MY_API_KEY
}

# day iteration from here:
# http://stackoverflow.com/questions/7274267/print-all-day-dates-between-two-dates
start_date = date(2019, 12, 20)
end_date = date(2020, 2, 10)
dayrange = range((end_date - start_date).days + 1)
for daycount in dayrange:
    dt = start_date + timedelta(days=daycount)
    datestr = dt.strftime('%Y-%m-%d')
    fname = join(ARTICLES_DIR, datestr + '.json')
    if not exists(fname):
        # then let's download it
        print("Downloading", datestr)
        all_results = []
        my_params['from-date'] = datestr
        my_params['to-date'] = datestr
        current_page = 1
        total_pages = 1
        while current_page <= total_pages:
            print("...page", current_page)
            my_params['page'] = current_page
            resp = requests.get(API_ENDPOINT, my_params)
            print(resp.url)
            data = resp.json()
            print(data)
            all_results.extend(data['response']['results'])
            # if there is more than one page
            current_page += 1
            total_pages = data['response']['pages']

        with open(fname, 'w') as f:
            print("Writing to", fname, len(all_results), "articles..")
            # re-serialize it for pretty indentation
            f.write(json.dumps(all_results, indent=2))
