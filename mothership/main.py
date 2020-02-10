import requests
from bs4 import BeautifulSoup

URLs = ["mothership.sg/category/news"]

for url in URLs:
    sourceCode = requests.get("http://" + str(url))

    soup1 = BeautifulSoup(sourceCode.content, "lxml")

    for div in soup1.find_all("div", class_="ind-article"):
        for a in div.find_all("a"):
            if "mothership.sg" in a.get("href") and "corona" in a.get("href"):
                print(a.get("href"))
                article_url = a.get("href")
                # article_sourceCode = requests.get("http://" + str(article_url))
