from time import sleep

from bs4 import BeautifulSoup

# open browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from tqdm import tqdm

home = 'https://www.theonlinecitizen.com/'
recrawl = True

if recrawl:
    page_url = home
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

    i = 0
    try:
        for x in tqdm(range(300)):
            body_element.send_keys(Keys.CONTROL + Keys.END)
            sleep(1)

    except KeyboardInterrupt as e:
        pass

    content = browser.page_source
    with open("data/news_2.html", "w") as f:
        f.write(content)
    browser.close()

html = open('data/news_2.html', 'r')
content = html.read()
soup1 = BeautifulSoup(content, "lxml")
# print(soup1)

articles = soup1.find_all('article')
print(len(articles))
_num = 0
all_urls = []
for article in articles:
    divs = article.find_all('div')
    for div in divs:
        if 'jeg_postblock_content' in div.get('class'):
            for a in div.find_all("a"):
                if "theonlinecitizen.com" in a.get("href"):
                    print(a.get("href"))
                    all_urls.append(a.get("href"))
                    _num += 1
                    break
print(_num)

with open('data/all_urls_new.txt', 'w+') as URLS:
    for url in all_urls:
        URLS.write(url + '\n')
        # get_data(url)
