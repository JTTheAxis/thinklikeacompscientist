import turtle

"ONE"
turtle.setup(400,500)                # Determine the window size
wn = turtle.Screen()                 # Get a reference to the window
wn.title("Handling keypresses!")     # Change the window title
wn.bgcolor("lightgreen")             # Set the background color
hec = turtle.Turtle()               # Create our favorite turtle
hec.shape("turtle")
size=5
hec.pensize(size)

# The next four functions are our "event handlers".
def h1():
   hec.forward(30)

def h2():
   hec.left(45)

def h3():
   hec.right(45)

def h4():
    wn.bye()                        # Close down the turtle window
    
def red():
   hec.color("red")

def blue():
   hec.color("blue")
   
def green():
   hec.color("green")
   
def grow():
   global size
   if size < 20:
      size+=1
      hec.pensize(size)
      
def shrink():
   global size
   if size > 1:
      size+=-1
      hec.pensize(size)
      
def cloak():
   hec.hideturtle()
   
def armor():
   hec.showturtle()
   
def disappear():
   hec.penup()
   
def appear():
   hec.pendown()

# These lines "wire up" keypresses to the handlers we've defined.
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")
wn.onkey(red, "r")
wn.onkey(blue, "b")
wn.onkey(green, "g")
wn.onkey(grow, "=")
wn.onkey(shrink, "-")
wn.onkey(cloak, "c")
wn.onkey(armor, "a")
wn.onkey(disappear, "m")
wn.onkey(appear, "v")

# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
wn.listen()
wn.mainloop()

"TWO"
turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()

def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()

draw_housing()

tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red.  We number these states  0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.

# This variable holds the current state of the machine
state_num = 0


def advance_state_machine():
    global state_num
    if state_num == 0:       # Transition from state 0 to state 1
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1
        wn.ontimer(advance_state_machine, 2000)
    elif state_num == 1:     # Transition from state 1 to state 2
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2
        wn.ontimer(advance_state_machine, 10000)
    else:                    # Transition from state 2 to state 0
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0
        wn.ontimer(advance_state_machine, 10000)

# Bind the event handler to the space key.

wn.ontimer(advance_state_machine, 10000)

wn.listen()                      # Listen for events
wn.mainloop()

"THREE"
turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Blazing Light")
wn.bgcolor("lightgreen")
hec= turtle.Turtle()
lyn= turtle.Turtle()
eli= turtle.Turtle()

def draw_light():
    hec.pensize(3)
    hec.color("black", "darkgrey")
    hec.penup()
    hec.pendown()
    hec.begin_fill()
    hec.forward(80)
    hec.left(90)
    hec.forward(200)
    hec.circle(40, 180)
    hec.forward(200)
    hec.left(90)
    hec.end_fill()
    
draw_light()

def light_setup():
    hec.penup()
    hec.forward(40)
    hec.left(90)
    hec.forward(50)
    hec.shape("circle")
    hec.fillcolor("green")
    hec.shapesize(3)
    
    lyn.forward(40)
    lyn.left(90)
    lyn.forward(120)
    lyn.shape("circle")
    lyn.fillcolor("orange")
    lyn.shapesize(3)
    lyn.hideturtle()
    
    eli.forward(40)
    eli.left(90)
    eli.forward(190)
    eli.shape("circle")
    eli.fillcolor("red")
    eli.shapesize(3)
    eli.hideturtle()

light_setup()

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red.  We number these states  0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.

# This variable holds the current state of the machine
state_num = 0

def three_heroes():
    global state_num
    if state_num == 0:       # Transition from state 0 to state 1
        hec.hideturtle()
        lyn.showturtle()
        state_num = 1
        wn.ontimer(three_heroes, 2000)
    elif state_num == 1:     # Transition from state 1 to state 2
        lyn.hideturtle()
        eli.showturtle()
        state_num = 2
        wn.ontimer(three_heroes, 5000)
    else:                    # Transition from state 2 to state 0
        eli.hideturtle()
        hec.showturtle()
        state_num = 0
        wn.ontimer(three_heroes, 5000)

wn.ontimer(three_heroes, 5000)
wn.listen()                      # Listen for events
wn.mainloop()

"FOUR"
turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Blazing Light")
wn.bgcolor("lightgreen")
hec= turtle.Turtle()
lyn= turtle.Turtle()
eli= turtle.Turtle()

def draw_light():
    hec.pensize(3)
    hec.color("black", "darkgrey")
    hec.penup()
    hec.pendown()
    hec.begin_fill()
    hec.forward(80)
    hec.left(90)
    hec.forward(200)
    hec.circle(40, 180)
    hec.forward(200)
    hec.left(90)
    hec.end_fill()
    
draw_light()

def light_setup():
    hec.penup()
    hec.forward(40)
    hec.left(90)
    hec.forward(50)
    hec.shape("circle")
    hec.fillcolor("green")
    hec.shapesize(3)
    
    lyn.forward(40)
    lyn.left(90)
    lyn.forward(120)
    lyn.shape("circle")
    lyn.fillcolor("grey")
    lyn.shapesize(3)
    
    eli.forward(40)
    eli.left(90)
    eli.forward(190)
    eli.shape("circle")
    eli.fillcolor("grey")
    eli.shapesize(3)

light_setup()

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red.  We number these states  0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.

# This variable holds the current state of the machine
state_num = 0

def three_heroes():
    global state_num
    if state_num == 0:       # Transition from state 0 to state 1
        hec.fillcolor("grey")
        lyn.fillcolor("yellow")
        state_num = 1
        wn.ontimer(three_heroes, 2000)
    elif state_num == 1:     # Transition from state 1 to state 2
        lyn.fillcolor("grey")
        eli.fillcolor("red")
        state_num = 2
        wn.ontimer(three_heroes, 5000)
    else:                    # Transition from state 2 to state 0
        eli.fillcolor("grey")
        hec.fillcolor("green")
        state_num = 0
        wn.ontimer(three_heroes, 5000)

wn.ontimer(three_heroes, 5000)
wn.listen()                      # Listen for events
wn.mainloop()

"FIVE"
turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Blazing Light")
wn.bgcolor("lightgreen")
hec= turtle.Turtle()
lyn= turtle.Turtle()
eli= turtle.Turtle()

def draw_light():
    hec.pensize(3)
    hec.color("black", "darkgrey")
    hec.penup()
    hec.pendown()
    hec.begin_fill()
    hec.forward(80)
    hec.left(90)
    hec.forward(200)
    hec.circle(40, 180)
    hec.forward(200)
    hec.left(90)
    hec.end_fill()
    
draw_light()

def light_setup():
    hec.penup()
    hec.forward(40)
    hec.left(90)
    hec.forward(50)
    hec.shape("circle")
    hec.fillcolor("green")
    hec.shapesize(3)
    
    lyn.forward(40)
    lyn.left(90)
    lyn.forward(120)
    lyn.shape("circle")
    lyn.fillcolor("grey")
    lyn.shapesize(3)
    
    eli.forward(40)
    eli.left(90)
    eli.forward(190)
    eli.shape("circle")
    eli.fillcolor("grey")
    eli.shapesize(3)

light_setup()

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red.  We number these states  0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.

# This variable holds the current state of the machine
state_num = 0

def three_heroes():
    global state_num
    if state_num == 0:
        lyn.fillcolor("yellow")
        state_num=1
        wn.ontimer(three_heroes, 1000)
    elif state_num == 1:       # Transition from state 0 to state 1
        hec.fillcolor("grey")
        lyn.fillcolor("yellow")
        state_num = 2
        wn.ontimer(three_heroes, 1000)
    elif state_num == 2:     # Transition from state 1 to state 2
        lyn.fillcolor("grey")
        eli.fillcolor("red")
        state_num = 3
        wn.ontimer(three_heroes, 2000)
    else:                    # Transition from state 2 to state 0
        eli.fillcolor("grey")
        hec.fillcolor("green")
        state_num = 0
        wn.ontimer(three_heroes, 3000)

wn.ontimer(three_heroes, 3000)
wn.listen()                      # Listen for events
wn.mainloop()