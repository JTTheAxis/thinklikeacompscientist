import turtle, sys, os
from math import *
from unit_tester import *
#wn=turtle.Screen()
#wn.bgcolor("light green")
#wn.title("Recursion Practice")
#hec=turtle.Turtle()
#hec.color("dark green")
#hec.pensize(5)
#hec.shape("turtle")
#hec.speed(0)

"ONE"
def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(t, order-1, size/3)
            t.left(angle)
    
def snowflake(t, order, size):
    for n in range(2):
        koch(t, order, size)
        t.right(120)
        koch(t, order-1, size/3)
        t.left(60)
        koch(t, order-1, size/3)
        t.right(120)
    
#snowflake(hec, 3, 200)

"TWO"
def cesaro(t, order, size, angle):
    if order==0:
        t.forward(size)
    else:
        cesaro(t, order-1, size/2, angle)
        t.right(angle)
        cesaro(t, order-1, size/2, angle)
        t.left(angle*2)
        cesaro(t, order-1, size/2, angle)
        t.right(angle)
        cesaro(t, order-1, size/2, angle)
        
def cesaro_square(t, order, size, angle):
    for n in range(4):
        cesaro(t, order, size,angle)
        t.right(90)

def equal_area(t, order, size, angle):
    width=size*(sin(radians(10))/sin(radians(85)))
    height=sqrt(size**2-(width/2)**2)
    n=order    
    area1=size**2
    area2=(size+(n)*width)**2-2*n*(width*height)
    ratio=area1/area2
    size=size*ratio
    cesaro_square(t, order, size, angle)
     
#cesaro(hec, 1, 200)
#equal_area(hec, 3, 200, 85)

"THREE"
def rtriangle(t, order, size):
    if order==0:
        for i in range(3):
            t.forward(size)
            t.left(120)
    else:
        rtriangle(t, order-1, size/2)
        t.forward(size/2)
        rtriangle(t, order-1, size/2)
        t.forward(size/2)
        t.left(120)
        t.forward(size/2)
        rtriangle(t, order-1, size/2)
        t.back(size/2)
        t.right(120)
        t.back(size)
              
#rtriangle(hec, 3, 200)

def colortriangle(t, order, size, color=-1):
    if order==0:
        for i in range(3):
            t.forward(size)
            t.left(120)
    else:
        if color==0:
            t.color("red")
        colortriangle(t, order-1, size/2, color-1)
        t.penup()
        t.forward(size/2)
        t.pendown()
        if color==0:
            t.color("blue")
        colortriangle(t, order-1, size/2, color-1)
        t.penup()
        t.forward(size/2)
        t.left(120)
        t.forward(size/2)
        t.left(60)
        t.forward(size/2)
        t.right(180)
        t.pendown()
        if color==0:
            t.color("dark green")
        colortriangle(t, order-1, size/2, color-1)
        t.penup()
        t.forward(size/2)
        t.left(120)
        t.back(size/2)
        t.right(120)
        t.back(size)
        t.pendown()
 
#colortriangle(hec, 4, 300, 2)  
#wn.mainloop()

"FIVE"
def recursive_min(l):
    small=None
    first_time=True
    for t in l:
        if type(t)==type([]):
            val=recursive_min(t)
        else:
            val=t
            
        if first_time or val < small:
            small=val
            first_time=False
                
    return small
        
#test(recursive_min([2, 9, [1, 13], 8, 6]) == 1)
#test(recursive_min([2, [[100, 1], 90], [10, 13], 8, 6]) == 1)
#test(recursive_min([2, [[13, -7], 90], [1, 100], 8, 6]) == -7)
#test(recursive_min([[[-13, 7], 90], 2, [1, 100], 8, 6]) == -13)

"SIX"
def count(target, l):
    n=0
    for i in l:
        if type(i)==type([]):
            val=count(target, i)
            n+=val
        else:
            if target==i:
                n+=1
                
    return n

#test(count(2, [])==0)
#test(count(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]]) == 4)
#test(count(7, [[9, [7, 1, 13, 2], 8], [7, 6]]) == 2)
#test(count(15, [[9, [7, 1, 13, 2], 8], [2, 6]]) == 0)
#test(count(5, [[5, [5, [1, 5], 5], 5], [5, 6]]) == 6)
#test(count("a",[["this",["a",["thing","a"],"a"],"is"], ["a","easy"]]) == 4)
        
"SEVEN"
def flatten(l):
    s=[]
    for i in l:
        if type(i)==type([]):
            m=flatten(i)
            for x in m:
                s.append(x)          
        else:
            s.append(i)
    return s

#test(flatten([2,9,[2,1,13,2],8,[2,6]]) == [2,9,2,1,13,2,8,2,6])
#test(flatten([[9,[7,1,13,2],8],[7,6]]) == [9,7,1,13,2,8,7,6])
#test(flatten([[9,[7,1,13,2],8],[2,6]]) == [9,7,1,13,2,8,2,6])
#test(flatten([["this",["a",["thing"],"a"],"is"],["a","easy"]]) ==["this","a","thing","a","is","a","easy"])
#test(flatten([]) == [])

"EIGHT"
def fib(n):
    (a, b)=1, 1
    for i in range(n):
        (a, b) =(b, a+b)
    return a

#print(fib(1000))
##fib(1000) takes mere seconds to perform. The improved function simply re-assigns the tuples over and over in a loop rather than going all the way back down the list and then all the way back up. Tail recursion is similar in that it calculates before each recursion call, while normal recursion does the computations AFTER all of the calls have been satisfied, and is much more likely to result in overloading due to the recursion depth being exceeded.

"NINE"
#help("sys")
#sys.setrecursionlimit(2000)
#print(sys.getrecursionlimit())
##It is worth noting that the default maximum recursion depth limit in python is 1150. However, this can be set to any real positive number using setrecursionlimit().

"TEN"
def get_dirlist(path):
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist

def fullfiles(path):
    compfiles=[]
    dirlist=get_dirlist(path)
    for f in dirlist:
        f=path+"\\"+f
        if os.path.isdir(f):
            l=fullfiles(f)
            for i in l:
                compfiles.append(i)
        else:
            compfiles.append(f)  
    return compfiles

#help("os")
#print(fullfiles(r"C:\Users\JXYTi\Desktop\Jason's Files\Programming\Python\How to think like a Computer Scientist"))
##Key to remember here is to put r in front of the string to convert it to a raw string.
"ELEVEN"
##get_dirlist() was added to both litter.py and cleanup.py before anything else
##below code added to litter.py
loc=r"C:\Users\JXYTi\Desktop\Test"
       
def litter(root):
    ##root is the directory in which to begin littering. 
    os.chdir(root) 
    trash=open("trash.txt", "w")
    trash.write("nahyuta best prosecutor, chitoge best girl")
    trash.close()
    d=get_dirlist(root)
    for f in d:
        f=root+"\\"+f
        if os.path.isdir(f):
            litter(f)

#litter(loc)

##below code is added to cleanup.py
loc=r"C:\Users\JXYTi\Desktop\Test"

def cleanup(root, target):
    ##root is the directory in which to begin cleaning, target is the file that is to be removed.
    d=get_dirlist(root)
    for f in d:
        if f==target:
            f=root+"\\"+f
            os.remove(f)            
        else:
            f=root+"\\"+f
        if os.path.isdir(f):
            cleanup(f, target)   

#cleanup(loc, "trash.txt")

