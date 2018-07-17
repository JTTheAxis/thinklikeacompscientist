import string

"ONE"
eval("Python"[1])=="n"
eval("Strings are sequences of characters."[5])=="g"
eval(len("wonderful"))==9
eval("Mystery"[:4])=="Myste"
eval("p" in "Pineapple")==True
eval("apple" in "Pineapple")==True
eval("pear" not in "Pineapple")=True
eval("apple" > "pineapple")==False
eval("pineapple" < "Peach")==False

"TWO"
prefixes= "JKLMNOPQ"
suffix="ack"

for letter in prefixes:
    if letter=="Q" or letter=="O":
        print(letter + "u" + suffix)
    else:
        print(letter + suffix)
        
"THREE"
def count_letters(letter):
    string=input()
    letter=str(letter)
    count=0
    for char in string:
        if char==letter:
            count+=1
    print(count)
            
QTHREE=count_letters("e")
print(QTHREE)

"FOUR"
def count_letters(string, letter):
    count=0
    newlocate=0
    locate=string.find(letter)
    while locate != -1:
        newlocate=locate+1
        locate=string.find(letter, newlocate)
        count+=1
    print(count)
Q_FOUR=count_letters("meme", "e")

"FIVE"
quote="""War... does not determine who is right... only who is left!"""
def remove_punc(para, letter):
    new_para=""
    count=0
    word=0
    for char in para:
        if char not in string.punctuation:
            new_para+=char
    new_para=new_para.split()
    for i in new_para:
        count+=1
        if i.count(letter)>0:
            word+=1
    percent=word/count*100
    if letter=="a"or letter=="e" or letter==i or letter=="o" or letter=="u":
        print("Your text has {0} words. {1}({2:.1f}%),of these words contain an {3}.".format(count, word, percent, letter))
    else:
        print("Your text has {0} words. {1}({2:.1f}%),of these words contain a {3}.".format(count, word, percent, letter))
Q_FIVE=remove_punc(quote, "e")

"SIX"
layout="{0:>2}{1:<5}{2:>2}{3:>4}{4:>4}{5:>4}{6:>4}{7:>4}{8:>4}{9:>4}{10:>4}{11:>4}{12:>4}{13:>4}"
print(layout.format("", "", "1", "2", "3", "4","5","6","7","8","9","10","11","12"))
print(layout.format("", ":-----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "-----", ""))
for i in range(1,13):
    print(layout.format(i, ":", i, i*2, i*3, i*4, i*5, i*6, i*7, i*8, i*9, i*10, i*11, i*12))
    
"SEVEN"
def reverse(word):
    word=word[::-1]
    return word
print(reverse("meme"))

"EIGHT"
def mirror(word):
    word+=reverse(word)
    return word
print(mirror("master"))

"NINE"
def remove_letter(letter, word):
    new=""
    for char in word:
        if char!=letter:
            new+=char
    return new
print(remove_letter("e", "meme"))

"TEN"
def is_palindrome(word):
    pal=reverse(word)
    return word==pal
print(is_palindrome("racecar"))

"ELEVEN"
def count(sect, word):
    count=0
    cv=0
    while cv < len(word):
        cv=word.find(sect,cv)
        if cv==-1:
            return count
        cv+=1
        count+=1
    return count
print(count("ana", "banana"))

"TWELVE"
def remove(sect, word):
    final=""
    p=word.find(sect)
    if p==-1:
        return word
    for c in word[:p]:
        final+=c
    for c in word[p+len(sect):]:
        final+=c
    return final
print(remove("cyc", "bicycle"))

"THIRTEEN"
def remove_all(sect, word):
    final=""
    cv=word.find(sect)
    if cv==-1:
        return word
    for c in word[:cv]:
        final+=c
    cv+=len(sect)
    while cv < len(word):
        p=word.find(sect,cv)
        if p==-1:
            for c in word[cv:]:
                final+=c
            return final
        for c in word[cv:p]:
            final+=c
        cv=p
        cv+=len(sect)