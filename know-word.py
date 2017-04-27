#!/usr/bin/python
import re
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn

def rebort(filename):
    raw_datas = open(filename, 'r+')
    sentence0 = str(raw_datas.read())
    sentence = sentence0.lower()
    tokens = word_tokenize(sentence)
    counts = Counter(tokens)
    d = []
    d.append(counts)
    words = re.findall(r'[A-Za-z]+', str(d))
    datas = open('words.txt', 'r+')
    text = datas.read()
    for x in words:
        y=str(wn.morphy(x))
        myMatch = re.search(y, text)
        if not(myMatch):
            print(y)
            datas.writelines(y + '\n')
    datas.close()

sentence = str(input("please input file directory \n>"))
# sentence='know-word.py'
rebort(sentence)

