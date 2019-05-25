#!/usr/bin/python
import re
import pysrt
import sys
import argv

# fileName= (argv.k(sys.argv[1:]))
fileName='zm.srt'
raw_datas= pysrt.open(fileName)
sentence=''
for line in raw_datas:
    sentence=sentence+str(line)

datas = open('out.srt', 'r+')
datas.truncate()
sentenceSplit = filter(None, sentence.split("\n"))
sentenceSplit2 = filter(None, sentence.split("\n"))
a = 0
b = 0
unknown = open("temp.txt", 'r+')
unknown_sentence = str(unknown.read())
d = []
words = re.findall(r'[A-Za-z]+', str(unknown_sentence))
for t in sentenceSplit:
    d.append(t)
for s in sentenceSplit2:
    k = re.findall(r'[A-Za-z]+', str(s))
    if (k):
        for y in words:
            myMatch = re.search(y, s)
            if (myMatch):
                print(y)
                b = 1
        if b == 1:
            datas.writelines(d[a - 3])
            datas.writelines("\n")
            datas.writelines(d[a - 2])
            datas.writelines("\n")
            datas.writelines(d[a - 1])
            datas.writelines("\n")
            datas.writelines(d[a])
            datas.writelines("\n")
            datas.writelines("\n")
    a = a + 1
    b = 0
datas.close()
unknown.close()
