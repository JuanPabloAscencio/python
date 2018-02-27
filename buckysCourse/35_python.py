import requests
from bs4 import BeautifulSoup
import operator


def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "lxml")
    for post_text in soup.findAll("h2"):
        content = post_text.string
        words = content.lower().split()
        for each_word in words:
            print(each_word)
            word_list.append(each_word)
    print(word_list)
#    print(source_code)

start("http://www.twitter.com")
