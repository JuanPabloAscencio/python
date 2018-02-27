import requests
from bs4 import BeautifulSoup

def spider(max_pages):
    page = 1
    while page <= max_pages:
        url = "http://www.9gag.com"
        source_code = requests.get(url)
        text_file = source_code.text
        soup = BeautifulSoup(text_file, "lxml")
        for link in soup.findAll("h1"):
            link = link.string
            #print(link)
        page =+ 1
spider(1)

def single_post_likes()
