import os
#ex. 1: handling file search
filename = input("Enter a file name: ")
try:
    f = open(filename, "r")
    file=f.read()
    f.close()
    print(file)
except:
    print("There is no file named", filename)
    
# This is the preferred way to check if a file exists.
if os.path.isfile("c:/temp/testdata.txt"):
    ...
    
#ex.2: a function to return one's age, "raising" a value error if the age input is less than 0. 
def get_age():
    age = int(input("Please enter your age: "))
    if age < 0:
        # Create a new instance of an exception
        my_error = ValueError("{0} is not a valid age.".format(age))
        raise my_error
    return age

#get_age()

#recursion_depth from chapter 18, but with a custom error line. 
def recursion_depth(number):
    print("Recursion depth number", number)
    try:
        recursion_depth(number + 1)
    except:
        print("I cannot go any deeper into this wormhole.")

recursion_depth(0)

#ex. 3: the finally clause in the try statement


def show_poly():
    try:
        win = turtle.Screen()   # Grab/create a resource, e.g. a window
        tess = turtle.Turtle()

        # This dialog could be cancelled,
        #   or the conversion to int might fail, or n might be zero.
        n = int(input("How many sides do you want in your polygon?"))
        angle = 360 / n
        for i in range(n):      # Draw the polygon
            tess.forward(10)
            tess.left(angle)
        time.sleep(3)           # Make program wait a few seconds
    finally: #The finally statement occurs no matter what, whether the try statement is successful or returns an error. This is because one will always want the window to be closed after the events in the try statement.
        win.bye()               # Close the turtle's window
        win.mainloop()

show_poly()
show_poly()
show_poly()