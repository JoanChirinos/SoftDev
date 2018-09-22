# Joan Chirinos
# SoftDev1 pd08
# K06 -- StI/O: Divine your Destiny!
# 2018-09-22

from random import random

def read(filename):
    straw = open(filename, 'r')
    text = straw.read()
    straw.close
    return text

def toDict(text):
    d = {}
    lines = text.split('\n')[1:]
    while (len(lines) > 0 and lines[-1] == ''):
        lines = lines[:-1]
    for line in lines:
        temp = line.rsplit(',', 1)
        d[temp[0].strip('"')] = float(temp[1])
    return d

def getRandom(d):
    total = d['Total']
    goal = random() * total
    for key in d.keys():
        goal -= d[key]
        if (goal < 0):
            return key
    return 'Something went horribly wrong Dx'

def go():
    return getRandom(toDict(read('data/occupations.csv')))
