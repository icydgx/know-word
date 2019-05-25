#!/usr/bin/python
import re
import pysrt
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn
import sys
import argv

def rebort(fileName):
    raw_datas= pysrt.open(fileName)
    sentence=''
    for line in raw_datas:
        sentence=sentence+str(line)
    a=open('temp.txt', "r+")
    a.seek(0)
    a.truncate()   #清空文件
    #sentence = str(raw_datas)
    tokens = word_tokenize(sentence)
    counts = Counter(tokens)
    d = [] 
    d.append(counts)
    words = re.findall(r'[A-Za-z]+', str(d))
    datas = open('words.txt', 'r+')
    text = datas.read()

    i=0
    for x in words:
        xLower=x.lower()
        firstMatch = re.search(xLower, text)
        secondMatch=re.search(y,text)
        if not(firstMatch):
            if not (secondMatch): 
                i=i+1
                print(x)
                a.writelines(x+'\n')
#            datas.writelines(y + '\n')
    print("unknow words number is",i)
    a.close()
    datas.close()

fileName= (argv.k(sys.argv[1:]))
rebort(fileName)
