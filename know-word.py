#!/usr/bin/python
import re
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn

def rebort(filename):
    raw_datas = open(filename, 'r+')
    sentence = str(raw_datas.read())
    # sentence = sentence0.lower()
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
            datas.writelines(y + '\n')
    print("unknow words number is",i)
    datas.close()

# sentence = str(input("please input file directory \n>"))
sentence='know-word.py'
rebort(sentence)

