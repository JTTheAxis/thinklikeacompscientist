import string 
"ONE"
#The range function has three different arguments, start, stop, and step, the first and third of which are optional. 
#If start < stop, then the function will proceed to make a list from start to stop. If start > stop, then the function will make a list of the range in reverse, due to the list starting at the largest number in the range. 
#If step is positive, then the function will move through the list normally if start > stop, and the same can be said for a negative step and when start < stop. However, when step is positive and start < stop, or step is negative and start > stop, the list turns up empty due to the list moving in a direction with no terms specified. 

"TWO"
#import turtle

#tess = turtle.Turtle()
#alex = tess
#alex.color("hotpink")
#In this fragment, only one turtle instance is created. This is because tess is first assigned as a turtle, but then alex is set equal to tess. In lists, if variable b is set equal to list a, then they are referring to the same list. Similarly, if alex is equal to tess, a turtle, then alex consequently must be set to the same turtle that tess is, and they are therefore one and the same. 

"THREE"
a= [1,2,3]
b= a[:]
b[0]=5
#Before line 4: a=[1,2,3], b=[1,2,3]
#After line 4: a=[1,2,3], b=[5,2,3]

"FOUR"
this = ["I", "am", "not", "a", "crook"]
that = ["I", "am", "not", "a", "crook"]
print("Test 1: {0}".format(this is that))
that = this
print("Test 2: {0}".format(this is that))

#Test one will be false, but since that is set equal to this before test two, test 2 will return true. At the beginning, this and that refer to two lists that are equal to each other, but the two variables do not return the same list, which is why test one will return false. Conversely, by setting that equal to this, the two are linked and are therefore now referring to the same list, rendering test two true. 

"FIVE"
def add_vectors(u, v):
    w=[]
    for (t, x) in enumerate(u):
        w+=u[t]+v[t]
    return w

"SIX"
def scalar_mult(s, v):
    l=[]
    for x in v:
        x=x*s
        l.append(x)
    return l

print(scalar_mult(5, [1,1600, 1900]))

"SEVEN"
def dot_product(u, v):
    l=0
    for (x, s) in enumerate(u):
        s=u[x]*v[x]
        l+=s
    return l

"EIGHT"
def cross_product(u, v):
    total=0
    for (x,s) in enumerate(u):
        if x!=2:
            s=(u[x]*v[x+1])-(u[x+1]*v[x])
        else:
            s=(u[x]*v[0])-(u[0]*v[x])
        total+=s**2
    total=total**0.5
    return total

#Tests:
#test(cross_product([3, -3, 1], [4, 9, 2])==1750**0.5)
#test(cross_product([3,-3,1], [-12,12,-4])==0)
#test(cross_product([3,-1,5], [0, 4, -2])==504**0.5)

"NINE"
song="The rain in Spain...      a "
print(song)
print(" ".join(song.split()))
#In most cases, the relationship between " ".join(song.split()) and song is how one would expect: the song is split into every word, and then put back together as normal. However, splitting the song does not include each space as a different term in the list. Therefore, if one was to put multiple spaces in a row between words, the song before and after being split and rejoined would only have one space in the location where the multiple spaces in a row were placed. In conclusion, one can say that the relationship between song and join is different when the string assigned to song contains more than one space in a row.

"TEN"
def replace(s, old, new):
    n=s.split()
    for (t, i) in enumerate(n):
        if old in i:
            l=i.split(old)
            for (s, x) in enumerate(l):
                if s%2==1:
                    l.insert(s, new)
            i="".join(l)
        n[t]=i
    return " ".join(n)

import string
def swap(x, y):      # Incorrect version
    print("before swap statement: x:", x, "y:", y)
    (x, y) = (y, x)
    print("after swap statement: x:", x, "y:", y)

a = ["This", "is", "fun"]
b = [2,3,4]
swap(a, b)
print(a, b)
print("before swap function call: a:", a, "b:", b)
print("after swap function call: a:", a, "b:", b)
#The above swap function fails because it only assigns the local variables, or the ones exclusive to the function itself, the value of the other. Variables a and b, which reside outside of the function, are not targeted by this change due to how variables always recognize the lists that are assigned to them as seperate lists, even if said lists are exactly the same. 