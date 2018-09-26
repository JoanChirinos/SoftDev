# Team StickyToes
# Joan Chirinos, Johnny Wong
# K12 -- 
# 2018-09-25

# importing relevant fxn from pkg random
from random import random

########## UTILITY FXNS ##########

# simple file reading
# returns text file contents as string
def read(filename):
    straw = open(filename, 'r')
    text = straw.read()
    straw.close
    return text

# takes string as arg
# returns dict
# Used to turn the string from read() into a workable dict
def toDict(text):
    d = {} #init dict
    lines = text.split('\n')[1:] #split text into lines
    while (len(lines) > 0 and lines[-1] == ''):
        lines = lines[:-1]
        
    #stores data from each line in dict as key: list
    for line in lines:
        temp = line.rsplit(',', 2)
        d[temp[0].strip('"')] = [float(temp[1]), temp[2]]
    return d

# gets random occupation and returns the key
def getRandom(d):
    total = d['Total'][0]
    goal = random() * total
    for key in d.keys():
        goal -= d[key][0]
        if (goal < 0):
            return key
    return 'Something went horribly wrong Dx'

########## END UTILITY FXNS ##########

# uses the 3 fxns above to get a random occupation
def getOcc():
    return getRandom(toDict(read('data/occupations.csv')))