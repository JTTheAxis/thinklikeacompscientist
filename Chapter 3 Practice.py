"ONE"
for i in range(5):
    print("We like Python's Turtles!")
    
"TWO"
"cellphone.color(blue)"
"cellphone.width(50)"
"cellphone.length(60)"
"cellphone.forward(40)"
"cellphone.left(90)"
"cellphone.forward(20)"

"THREE"
for month in ["January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]:
    print ("One of the months of the year is " + month + ".")

"FOUR"
#if tess is at heading 0, facing east, then the statement tess.left(3645) will make tess turn 45 degrees counter-clockwise. This is because every 360 degrees is a full circle, resulting in the object facing the same way it was before rotation. 3600/360=10, meaning she rotates 10 time,s and then proceeds to end turned 45 degrees counter-clockwise. 

"FIVE"
xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
print(xs)
for x in (xs):
    print(x**2)
total=0
for t in (xs):
    total= total+t
print(total)

"SIX"
#Constant Code
import turtle
wn=turtle.Screen()
wn.bgcolor("red")
wn.title("This is not a red screen")
Hec=turtle.Turtle()
Hec.color("dark green")
Hec.shape("turtle")
Hec.pensize(10)
Hec.speed(1)

#Triangle
#for i in range(3):
    #Hec.forward(50)
    #Hec.left(120)
  
#Square
#for i in range(4):
    #Hec.forward(50)
    #Hec.right(-90)
    
#Hexagon
#for i in range(6):
    #Hec.forward(80)
    #Hec.left(60)
    
#Octagon
#for i in range(8):
    #Hec.forward(100)
    #Hec.right(-45)

"SEVEN"
#for i in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
# Hec.forward(100)
# Hec.left(i)
 
"EIGHT"
#final_heading=0
#for i in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
#    final_heading=final_heading+i
#print("The pirate's final heading is " + str(final_heading) + " degrees.")

"NINE"
#The angle required would be 20 degrees.
#for i in range(17):
#    Hec.forward(30)
#    Hec.right(-20)

"ELEVEN"
#Hec.hideturtle()
#for angle in range(5):
    #Hec.forward(300)
    #Hec.right(144)

"TWELVE"
#Clock
Hec.speed(10)
for clock_arm in range(12):
    Hec.penup()
    Hec.forward(160)
    Hec.pendown()
    Hec.forward(20)
    Hec.penup()
    Hec.forward(20)
    Hec.stamp()
    Hec.backward(200)
    Hec.left(30)

"THIRTEEN"    
print(type(Hec))   
#The variable with a turtle assigned to it is classified as type "turtle.Turtle()".

wn.mainloop() 


