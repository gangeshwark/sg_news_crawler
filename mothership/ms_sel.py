from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

driver = webdriver.Firefox(executable_path='../geckodriver')
driver.get("https://www.mothership.sg/category/news/")

exit()


def get_data(url):
    driver = webdriver.Firefox(executable_path='//geckodriver')
    driver.get(url)
    headline = driver.find_elements_by_tag_name('h1').text
    publish_date = driver.find_element_by_class_name("publish-date").text
    print(headline)
    print(publish_date)
    source = 'Mothership'


def get_dat_bs(url):
    sourceCode = requests.get("http://" + str(url))
    soup1 = BeautifulSoup(sourceCode.content, "lxml")

    soup1.find('h1')


# assert "Python" in driver.title
load_more_button = driver.find_element_by_id("load-more")
for i in tqdm(range(200)):
    load_more_button.click()
    sleep(1)

sleep(3)

all_urls = []
for div in driver.find_elements_by_class_name('ind-article'):
    for a in div.find_elements_by_tag_name('a'):
        if "mothership.sg" in a.get_attribute("href"):
            print(a.get_attribute("href"))
            all_urls.append(a.get_attribute("href"))
            # get_data(a.get_attribute("href"))

driver.close()

with open('all_urls.txt', 'w+') as URLS:
    for url in all_urls:
        URLS.write(url + '\n')
        # get_data(url)
