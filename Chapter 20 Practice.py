from unit_tester import *
import wordtools as w
"ONE"
def lettercount(phrase):
    phrase=phrase.lower()
    phrase=phrase.replace(" ", "")
    letterlist={}
    for letter in phrase:
        letterlist[letter]=letterlist.get(letter, 0)+1
    letterkeys=list(letterlist.keys())
    letterkeys.sort()
    table=""
    for letter in letterkeys:
        if letter==letterkeys[len(letterkeys)-1]:
            table+="{0}{1:>3}".format(letter, letterlist[letter])
        else:
            table+="{0}{1:>3}".format(letter, letterlist[letter]) +"\n"
    return table
    
#print(lettercount("ThiS is String with Upper and lower case Letters"))

"TWO"
#a. 15
#b. 4
#c. True
#d. KeyError: 'pears'
#e. 0
#f. [apples, bananas, grapes, oranges]
#g. False

def add_fruit(inventory, fruit, quantity=0):
    current=inventory.get(fruit, 0)
    inventory[fruit]=current+quantity
    return 

new_inventory = {}
add_fruit(new_inventory, "strawberries", 10)
#test("strawberries" in new_inventory)
#test(new_inventory["strawberries"] == 10)
add_fruit(new_inventory, "strawberries", 25)
#test(new_inventory["strawberries"] == 35)
    
"THREE"
#below added to alice_words.py
myfile=open("alice_in_wonderland.txt", "r")
file=myfile.read()
myfile.close()
def wordrun(article):
    import wordtools as w
    layout="{0:<15}{1:^10}{2:<}"
    wordtable=""
    words=w.extract_words(article)
    worddict={}
    for w in words:
        worddict[w]=worddict.get(w, 0)+1
    wordlist=list(worddict.keys())
    wordlist.sort()
    wordtable+=layout.format("Words", "", "Count") + "\n"
    wordtable+=layout.format("===============", "==========", "======") + "\n"
    for key in wordlist:
        if key==wordlist[len(wordlist)-1]:
            wordtable+=layout.format(key, "", worddict[key])
        else:
            wordtable+=layout.format(key, "", worddict[key])+"\n"
    return wordtable

alice=open("alice_words.txt", "w")
alice.write(wordrun(file))
alice.close()
##The word "alice" appears 398 times throughout the entire book.

"FOUR"
handle=open("alice_in_wonderland.txt", "r")
alice=handle.read()
handle.close()
words=w.extract_words(alice)
#print(w.longestword(words))

##The longest word in "Alice in Wonderland" is disappointment, which is 14 characters long.