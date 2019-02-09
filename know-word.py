#!/usr/bin/python
import re
from collections import Counter

from nltk.corpus import wordnet as wn
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize


def rebort(filename):
    raw_datas = open(filename, 'r+')
    sentence = str(raw_datas.read())
    tokens = word_tokenize(sentence)
    counts = Counter(tokens)
    d = []
    d.append(counts)
    words = re.findall(r'[A-Za-z]+', str(d))
    datas = open('words.txt', 'r+')
    text = datas.read()

    snowball_stemmer = SnowballStemmer("english")

    i = 0
    for x in words:
        y = str(wn.morphy(x))
        z = str(snowball_stemmer.stem(x))
        yMatch = re.search(y, text)
        zMatch = re.search(z, text)
        if not yMatch and not zMatch:
            i = i + 1
            print(x)
            # datas.writelines(y + '\n')
            print("unknow words number is", i)
    datas.close()


sentence = str(input("please input file directory \n>"))
rebort(sentence)
