import turtle
def make_window(colr, ttle):
    w= turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w

def make_turtle(colr, sz, shp, spd):
    t=turtle.Turtle()
    t.color(colr)
    t.pensize(sz)
    t.shape(shp)
    t.speed(spd)
    
    return t
    
wn = make_window("yellow", "This is not a gold screen")
Hec = make_turtle("darkblue", 10, "turtle", 0)
Lyn = make_turtle("lightgreen", 2, "arrow", 0)
Eli = make_turtle("orange", 5, "classic", 0)

"ONE"
def draw_one(w, q):
    for i in range(q):
        for i in range(4):
            Hec.pendown()
            Hec.forward(w)
            Hec.left(90)
        Hec.penup()
        Hec.forward(2*w)
#Ex_One = draw_one(20, 5)

"TWO"
def draw_two(b):
    
    for i in range(5):
        for i in range(4):
            Lyn.forward(b)
            Lyn.left(90)  
        Lyn.penup()    
        for i in range(2):
            Lyn.right(90)
            Lyn.forward(20)
        Lyn.left(180)
        b=b+40
        Lyn.pendown()
        
#Ex_Two= draw_two(20)

"THREE"
def draw_poly(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.left(180 - 180*(n-2)/n)
#Ex_Three= draw_poly(Eli, 8, 50)

"FOUR"
def draw_prettyshape(l, angle, n):
    for i in range(n):
        for i in range(4):
            for i in range(4):
                Lyn.forward(l)
                Lyn.left(90)            
            Lyn.left(90)
        Lyn.left(angle)
        
#Ex_Four= draw_prettyshape(90, 360/20, 10)

"FIVE"
def draw_spiral(l, n):
    Eli.right(90)
    for i in range(n):
        Eli.forward(l)
        l=l+4
        Eli.right(90)
         
#Ex_Fivea= draw_spiral(4, 99)

def draw_wavy(l, n, angle): 
    Eli.right(angle)
    for i in range(n):
        Eli.forward(l)
        l=l+4
        Eli.right(angle)    
#Ex_Fiveb= draw_wavy(4, 97, 91)  

"SIX"
def draw_equitriangle(t, sz):
    draw_poly(t, 3, sz)
    
#Ex_Six= draw_equitriangle(Hec, 100)    

"SEVEN"
def sum_to(n):
    T= 0
    for i in range(n):
        T=T+i
    print(T)
    
#Ex_Seven= sum_to(10)

"EIGHT"
def area_of_circle(r):
    area = 3.14*(r**2)
    print(area)
Ex_Eight= area_of_circle(4)

"NINE"
def draw_star(l):
    for i in range(5):
        Hec.forward(l)
        Hec.right(144)   
        
#Ex_Nine= draw_star(100)

"TEN"
def draw_star_formation(n):
    for i in range(n):
        draw_star(100)
        Hec.penup()
        Hec.forward(300)
        Hec.right(144)
        Hec.pendown()
        
#Ex_Ten=draw_star_formation(5)
wn.mainloop()
    
