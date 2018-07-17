import math

#de Morgan's laws
#not (x and y) == (not x) or (not y)
#not (x or y) == (not x) and (not y)

"ONE"
#Weekday= int(input("What number is the day of the week?"))
#if Weekday==1:
#    print("Monday")
#elif Weekday==2:
#    print("Tuedsay")  
#elif Weekday==3:
#    print("Wednesday")
#elif Weekday==4:
#    print("Thursday")
#elif Weekday==5:
#    print("Friday")
#elif Weekday==6:
#    print("Saturday")
#elif Weekday==0:
#    print("Sunday")
#else:
#    print("Error, only weekdays please.")

"TWO"
def holiday_time(Departure):
    Duration=int(input("How many days will you be staying for?"))
    Day_Number=Departure + Duration
    if Day_Number % 7==1:
        print("You will return on a", "Monday")
    elif Day_Number % 7==2:
        print("You will return on a","Tuedsay")  
    elif Day_Number%7==3:
        print("You will return on a","Wednesday")
    elif Day_Number%7==4:
        print("You will return on a","Thursday")
    elif Day_Number%7==5:
        print("You will return on a","Friday")
    elif Day_Number%7==6:
        print("You will return on a","Saturday")
    elif Day_Number%7==0:
        print("You will return on a","Sunday")
My_Vacation= holiday_time(int(input("What day do you leave?")))

"THREE"
#a<=b
#a<b
#a<18 and day!=3
#a<18 and day ==3

"FOUR"
print(3==3)
#True
print(3!=3)
#False
print(3>=4)
#False
print(not(3<4))
#False

"FIVE"
#p q r   (not(p and q)) or r= not p or not q or r
#F F F    T
#F F T    T
#F T F    T
#F T T    T
#T F F    T
#T F T    T
#T T F    F
#T T T    T

"SIX"
def marking_scheme(Mark):
    if Mark >= 75:
        print(str(Mark), "First")
    elif Mark < 75 and Mark >= 70:
        print(str(Mark),"Upper Second")
    elif Mark < 70 and Mark >= 60:
        print(str(Mark),"Second")
    elif Mark < 60 and Mark >= 50:
        print(str(Mark),"Third")
    elif Mark < 50 and Mark >= 45:
        print(str(Mark),"F1 Support")
    elif Mark < 45 and Mark >= 40: 
        print(str(Mark),"F2")
    elif Mark < 40 and Mark >= 0:
        print(str(Mark),"F3")
    else: 
        print("Marks can't be negative, you fucking dolt.")
        
for Grade in [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50,49.9, 45, 44.9, 40, 39.9, 2, 0]:
    Calculating_Marks = marking_scheme(Grade)
    
import turtle
"SEVEN"
def draw_bar(t, height):
    t.speed(0)
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()           # Added this line
    t.left(90)
    t.forward(height)
    t.write("  "+ str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill() 
    t.penup()
    t.forward(10)
    t.pendown()
    
wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")
    
tess = turtle.Turtle()       # Create tess and set some attributes
tess.color("blue", "red")
tess.pensize(3)
    
xs = [48,117,200,240,160,260,220]
    
for a in xs:
    draw_bar(tess, a)
    
"EIGHT"
def draw_bar(t, height):
    if height >= 200:
        t.color("blue", "red")
    elif height < 200 and height >=100:
        t.color("blue", "yellow")
    elif height < 100 and height >= 0:
        t.color("blue", "green")    
    t.speed(0)
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()           # Added this line
    t.left(90)
    t.forward(height)
    t.write("  "+ str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill() 
    t.penup()
    t.forward(10)
    t.pendown()
    
wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")
    
tess = turtle.Turtle()       # Create tess and set some attributes
tess.pensize(3)
    
xs = [48,117,200,240,160,260,220]
    
for a in xs:
    draw_bar(tess, a)
    wn.mainloop()

"NINE"
def draw_bar(t, height):
    if height >= 200:
        t.color("blue", "red")
    elif height < 200 and height >=100:
        t.color("blue", "yellow")
    elif height < 100 and height >= 0:
        t.color("blue", "green")   
    else:
        t.color("black", "red")
    t.speed(1)
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()
    if height < 0:
        t.right(90)
        t.backward(height)
        t.write(" " + str(height))
        t.left(90)
        t.forward(40)
        t.left(90)
        t.backward(height)
        t.right(90)
    else:            
        t.left(90)
        t.forward(height)
        t.write("  "+str(height))
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(height)
        t.left(90)
    t.end_fill() 
    t.penup()
    t.forward(10)
    t.pendown()
    
wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")
    
tess = turtle.Turtle()       # Create tess and set some attributes
tess.pensize(3)
    
xs = [100, -100]
    
for a in xs:
    draw_bar(tess, a)  
    
"TEN"
def find_hypot(leg, short):
    square=leg**2 + short**2
    hypot=square**0.5
    return hypot
    
lowest_triangle=find_hypot(3,4)
print(lowest_triangle)

"ELEVEN"
def right_angled(leg, short, hypot):
    square=leg**2 + short**2
    if hypot==square**0.5:
        print("True")
    else:
        print("False")
    
sample_right=right_angled(4,3,5)
sample_left=right_angled(2,3,4)

"TWELVE"
def newright_angled(sideone, sidetwo, sidethree):
    if sideone > sidetwo and sideone > sidethree:
        print(sideone**2==sidetwo**2 + sidethree**2)
    elif sidetwo > sideone and sidetwo > sidethree:
        print(sidetwo**2==sideone**2 + sidethree**2)
    else:
        print(sidethree**2==sideone**2 +sidetwo**2)
    
sample_right=newright_angled(4,2,5)
sample_left=newright_angled(5,4,3)


import math
"THIRTEEN"
#just a tip about floats being inaccurate
a = math.sqrt(2.0)
print(a, a*a)
print(a*a == 2.0)
#non-terminating decimals will have to round/discard certain digits, leading to situations like the above.

    