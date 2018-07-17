"ONE"
import calendar
#cal = calendar.TextCalendar()
#cal.setfirstweekday(3)
##setfirstweekday() is a method that only takes numbers as arguments, where 0 is Sunday and 6 is Saturday.
#cal.pryear(2012)
##pryear takes a given year, and outputs the corresponding calendar for the entire year.
#cal.prmonth(2018, 7)
##While pryear prints a whole year's calendar, prmonth prints a month in a given year. It takes 2 arguments: the exact year and the month, which is represented by a number. 
#d = calendar.LocaleTextCalendar(0, "German")
#d.pryear(2012)
##localetextcalendar changes the month and day names to a specified language. Keep in mind, however, that certain languages such as Chinese and Japanese use symbols that can only be returned as unicode in the console. It takes 2 arguments, one being the starting day of the week, with the other being a string that specifies the language to be displayed.
#leap= calendar.isleap(2013)
#print(leap)
##calendar.isleap is a function that takes a single int as an argument, and returns True or False pending on whether or not the specified year is a leap year. It is a fruitful function because it returns a value of True or False, not None. 

"TWO"
import math
##There are a total of 44 functions included in the math module.
#print(math.ceil(2.1))
#print(math.floor(2.9))
##math.ceil takes a floating point argument and rounds it down to the nearest integer, while math.floor does the same but rounds up instead of down.
##Even if we are not using math.sqrt, it is still possible to calculate the square root of something by using x**0.5. Much like multiplication, where the effects of division can be done using x*0.5, the effects of square root can be done by using x**0.5, because it is the opposite of squaring. Squaring is to the power of 2, and square root is to the power of 0.5, similar to how double a number is x*2, but half of that same number is x*0.5. 
#print(math.e)
#print(math.pi)
##The two data constants in the math module are e (natural base of log) and pi (used in many aspects of circle mathematics). Tau is also a constant, but is simply 2pi, and could not be derived without the pre-existing pi.

"THREE"
##deepcopy creates copies of the objects in an original compound object/function into a new compound object/function. It differs from a shallow copy in that a shallow copy directly inserts the structure of the function, but not necessarily the exact elements. In essence, one can think of a shallow copy as assigning a new function equal to an old function, while deepcopying creates a clone of the old function with the exact same terms. Deepcopying would have come in handy in most of the function-creation exercises last chapter, as pure functions are recommended over modifying ones, meaning that creating copies of the lists and data would be better than modifying, which is the difference between deep and shallow copies. 

"FOUR"
import mymodule1_12; import mymodule2_12

#print((mymodule2_12.myage -mymodule1_12.myage)==(mymodule2_12.year-mymodule1_12.year))
##Because the above statement returns false, I have not had my birthday yet this year. 

"FIVE"
#print("My name is", __name__)
##When this is run, 3 statements are printed: My name is "mymodule1", "mymodule2", and "__main__" respectively. The imported modules have their names printed, but the file in which it is being run has its name returned as "__main__". This is because it is the main module as it is the one currently in use, not being imported from anywhere else. 
##After modifying "mymodule1", it only returns the statement where it says "This won't run if I'm imported." when running mymodule1. When running namespace, it is in fact imported, meaning that the second part of the statement has no reason to run. 

"SIX"
import this
##The Zen of Python, by Tim Peters
##Beautiful is better than ugly.
##Explicit is better than implicit.
##Simple is better than complex.
##Complex is better than complicated.
##Flat is better than nested.
##Sparse is better than dense.
##Readability counts.
##Special cases aren't special enough to break the rules.
##Although practicality beats purity.
##Errors should never pass silently.
##Unless explicitly silenced.
##In the face of ambiguity, refuse the temptation to guess.
##There should be one-- and preferably only one --obvious way to do it.
##Although that way may not be obvious at first unless you're Dutch.
##Now is better than never.
##Although never is often better than *right* now.
##If the implementation is hard to explain, it's a bad idea.
##If the implementation is easy to explain, it may be a good idea.
##Namespaces are one honking great idea -- let's do more of those!

"SEVEN"
from unit_tester import *
s = "If we took the bones out, it wouldn't be crunchy, would it?"
test(s.split()==s.split())
test(type(s.split())==list)
test(s.split("o")==["If we t", "", "k the b", "nes ", "ut, it w", "uldn't be crunchy, w", "uld it?"])
test(s.split("n")==["If we took the bo", "es out, it would", "'t be cru", "chy, would it?"])
test("0".join(s.split("o"))=="If we t00k the b0nes 0ut, it w0uldn't be crunchy, w0uld it?")

def myreplace(old, new, s):
    l=s
    l=l.split()
    l=" ".join(l)
    return new.join(l.split(old))

test(myreplace(",", ";", "this, that, and some other thing")=="this; that; and some other thing")

test(myreplace(" ", "**", "Words will now      be  separated by stars.") == "Words**will**now**be**separated**by**stars.")
l= "Words will now      be  separated by stars."

"EIGHT"
import string
from unit_tester import *
def cleanword(word):
    newword=""
    for c in word:
        if c not in string.punctuation:
            newword+=c
    return newword
test(cleanword("what?") == "what")
test(cleanword("'now!'") == "now")
test(cleanword("?+='w-o-r-d!,@$()'") ==  "word")

def has_dashdash(word):
    if "--" in word:
        return True
    else:
        return False
    
test(has_dashdash("distance--but"))
test(not has_dashdash("several"))
test(has_dashdash("spoke--"))
test(has_dashdash("distance--but"))
test(not has_dashdash("-yo-yo-"))

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

test(extract_words("Now is the time!  'Now', is the time? Yes, now.") ==
      ['now','is','the','time','now','is','the','time','yes','now'])
test(extract_words("she tried to curtsey as she spoke--fancy") ==
      ['she','tried','to','curtsey','as','she','spoke','fancy'])

def wordcount(word, seq):
    count=0
    for i in seq:
        if i==word:
            count+=1
    return count

test(wordcount("now", ["now","is","time","is","now","is","is"]) == 2)
test(wordcount("is", ["now","is","time","is","now","the","is"]) == 3)
test(wordcount("time", ["now","is","time","is","now","is","is"]) == 1)
test(wordcount("frog", ["now","is","time","is","now","is","is"]) == 0)

def wordset(seq):
    newseq=[]
    for word in seq:
        if word not in newseq:
            newseq.append(word)
            newseq.sort()
    return newseq

test(wordset(["now", "is", "time", "is", "now", "is", "is"]) ==
      ["is", "now", "time"])
test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) ==
      ["I", "a", "am", "is"])
test(wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) ==
      ["a", "am", "are", "be", "but", "is", "or"])

def longestword(seq):
    length=0
    for word in seq:
        if len(word) > length:
            length=len(word)
    return length

test(longestword(["a", "apple", "pear", "grape"]) == 5)
test(longestword(["a", "am", "I", "be"]) == 2)
test(longestword(["this","supercalifragilisticexpialidocious"]) == 34)
test(longestword([ ]) == 0)