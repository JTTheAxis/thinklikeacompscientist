import string
def cleanword(word):
    newword=""
    for c in word:
        if c not in string.punctuation:
            newword+=c
    return newword

def has_dashdash(word):
    if "--" in word:
        return True
    else:
        return False
    
def extract_words(phrase):
    phrase=phrase.lower()
    phrase=phrase.split()
    l=""
    for i in phrase:
        for c in i:
            if c in string.punctuation:
                i=i.replace(c, " ")
        i="".join(i)
        i+=" "
        l+=i
    l=l.split()
    return l

def wordcount(word, seq):
    count=0
    for i in seq:
        if i==word:
            count+=1
    return count

def wordset(seq):
    newseq=[]
    for word in seq:
        if word not in newseq:
            newseq.append(word)
            newseq.sort()
    return newseq

def longestword(seq):
    length=0
    for word in seq:
        if len(word) > length:
            length=len(word)
    return length