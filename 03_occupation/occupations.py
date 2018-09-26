# Team ThinkOfIt
# Vincent Chi, Joan Chirinos
# SoftDev1 pd08
# K06 -- StI/O: Divine your Destiny!
# 2018-09-13

# we don't need the whole random library
from random import random

# simple file reading + returning text
def read(filename):
    straw = open(filename, 'r')
    text = straw.read()
    straw.close
    return text

# turns the formatted text into a dictionary then returns it
def toDict(text):
    # init dict
    d = {}

    # turn into list for easy iteration
    # we throw away the first item because it's not important to us:
    # "Job Class,Percentage"
    lines = text.split('\n')[1:]

    # we often get blank lines at the end of the doc because of split,
    # so trim these
    while (len(lines) > 0 and lines[-1] == ''):
        lines = lines[:-1]
    
    # loops through lines in text
    for line in lines:
        # splits at last comma
        # why? We're not guaranteed that the name doesn't have commmas
        # but we're guaranteed that the number doesn't (why should a # < 100 have
        # commas?) Thus, if we split at the last comma we're left with the
        # occupation (possibly in quotes, so we strip them) and the %. So we good
        temp = line.rsplit(',', 1)
        # defines the quote-stripped occupation as the percentage in the dictionary
        d[temp[0].strip('"')] = float(temp[1])
    # once done, return the dict for the next part
    return d

# takes dict from toDict and returns weighted random occupation
def getRandom(d):
    # takes the total from the dict in order to do randomness right
    total = d['Total']

    # reason for goal + keys shall become clear after the rest of the fxn
    goal = random() * total

    # basically we iterate through the keys until our goal is exhausted
    # think of the choices on a # line. If A has a prob of 2.2 and B has a prob
    # of 1.1, A would occupy [0, 2.2) and B would occupy [2.2, 3.3). The same goes
    # for every choice. As we subtract from total, it's like traversing through
    # the # line
    for key in d.keys():
        goal -= d[key]
        if (goal < 0):
            return key
    return 'Something went horribly wrong Dx'

def go():
    return getRandom(toDict(read('occupations.csv')))

print(go())
