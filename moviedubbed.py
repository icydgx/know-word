#!/usr/bin/python
import re
import nltk
from collections import Counter
from nltk.stem.wordnet import WordNetLemmatizer


def rebort(filename):
    #     sentence = """Take the airship back to where the tower is, and head north from
    # there to find the Mana Tree where we really kill apples great great
    # ha..."""
    raw_datas = open(filename, 'r+',encoding='utf8')
    sentence0 = str(raw_datas.read())
    # print(sentence0)
    # sentence0=sentence0.decode('utf-16')
    # sentence0=sentence0.replace('\n', ' ')
    # sentence0=re.search(r'[A-Za-z]+',sentence0)
    # sentence0=sentence0.group()
    # print(sentence0)
    sentence = sentence0.lower()
    lmtzr = WordNetLemmatizer()
    # snowball_stemmer = SnowballStemmer("english")
    tokens = nltk.word_tokenize(sentence)

    # nonPunct=re.compile('.*[A-Za-z0-9].*')
    # filtered=[w for w in tokens if nonPunct.match(w)]
    counts = Counter(tokens)
    d = []
    d.append(counts)
    words = re.findall(r'[A-Za-z]+', str(d))
    # words[0]
    # print(words[3])
    datas = open('words.txt', 'r+',encoding='utf8')
    text = datas.read()
    for x in words:
        # print(tokens[x])
        y = lmtzr.lemmatize(x)
        myMatch = re.search(y, text)
        if not(myMatch):
            # most have one sentence
            # myMatch.group(0)
            bool(re.search("\b{0}\b".format(x),text))
            print(y)
            datas.writelines(y + '\n')
        # else:
        #     print(x)
        #     # print(y)
        #     # regex = re.compile(r".*\(.*'+y+'.*[.,?!]*\)")
        #     # result = regex.search(sentence0)
        #     # print(sentence0)
        #     # searchObj=re.search(r'.*[.](.*aoeu.*[.])',sentence)
        #     searchObj = re.search(r'(.*' + y + '.*[.,])' + '.*', sentence)
        #     if searchObj:

        #         # searchObj=re.search(r'',sentence0)

        #         print(searchObj.group(1))
            # searchObj=re.search(r'(.*'+y+'.*[.,])'+'.*',sentence)
            # if searchObj:

            # # searchObj=re.searnch(r'',sentence0)

            #     print(searchObj.group(1))

            # my name is good.you will shoot by me!i like you
            # good morning.i think emacs is great.i love you

            # print(myMatch.group(0)
            # )
            # print(y)

            # datas.writelines(y+'\n')
        # words = re.findall(r"[\w]+",sentence)

    datas.close()


# sentence = str(input("请输入文档路径\n>"))
# sentence='tmp.org'
# sentence = '/home/czj/Downloads/resident.evil.the.final.chapter.(2016).eng.1cd.(6873925)/Resident Evil The Final Chapter 2017 HD-TS x264-CPG.srt'
# sentence = './test.txt'
# sentence='Desperate.Housewives.S03E09.Beautiful.Girls.720p.WEB-DL.AAC2.0.h.264-TjHD.ch-eng.srt'
sentence='a.srt'
# print(sentence)
rebort(sentence)
# /home/czj/Videos/Desperate.Housewives.S03.720p.WEB-DL.AAC2.0.h.264-TjHD/Desperate.Housewives.S03E09.Beautiful.Girls.720p.WEB-DL.AAC2.0.h.264-TjHD.ch-eng.srt
