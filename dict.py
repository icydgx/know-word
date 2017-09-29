#!/usr/bin/python
import re
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn
import requests
from bs4 import BeautifulSoup
def rebort(filename):
    raw_datas = open(filename, 'r+')
    sentence = raw_datas.read()
    tokens = word_tokenize(sentence)
    counts = Counter(tokens)
    d = []
    d.append(counts)
    words = re.findall(r'[A-Za-z]+', str(d))
    datas = open('words.txt', 'r+')
    text = datas.read()

    i=0
    for x in words:
        y=str(wn.morphy(x))
        myMatch = re.search(y, text)
        if not(myMatch):
            i=i+1
            print(y)
            BASE_URL = "http://dict.cn/"+y

            html = requests.get(BASE_URL).text
            soup = BeautifulSoup(html, "html.parser")
            print(soup.strong.string)
            # datas.writelines(y + '\n')

    print("unknow words number is",i)
    datas.close()

# sentence = str(input("please input file directory \n>"))
sentence='Table of Contents.txt'
rebort(sentence)

