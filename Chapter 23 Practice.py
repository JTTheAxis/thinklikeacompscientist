import cards
"ONE"
#added to OldMaidGame 
def print_hands(self):
    for hand in self.hands:
        print(hand)
        
"TWO"
import turtle
class TurtleGTX(turtle.Turtle):
    import random
    rng=random.Random()    
    odometer=0
    tick=rng.randrange(1, 300)
    def fd(self, dist):
        self.test_tyre()
        for i in range(1, dist):
            if self.odometer==self.tick:
                break
            self.forward(1)
            self.odometer+=1
    def bk(self, dist):
        self.test_tyre()
        for i in range(1, dist):
            if self.odometer==self.tick:
                break
            self.back(1)
            self.odometer+=1       
    def jump(self, dist, spd):
        self.penup()
        self.speed(0)
        self.forward(dist)
        self.odometer+=dist
        self.pendown()
        self.speed(spd)
    def odm(self):
        print(self.odometer)
    def test_tyre(self):
        try:
            self.fd()
        except:
            if self.odometer==self.tick:
                print("TurtleGTX has broken down!")
    def change_tyre(self):   
        import random
        rng=random.Random()
        self.tick+=rng.randrange(1, 300) 


"THREE"
#Below added to GTX class
def test_tyre(self):
    try:
        self.fd()
    except:
        if self.odometer==self.tick:
            print("TurtleGTX has broken down!")
def change_tyre(self):   
    import random
    rng=random.Random()
    self.tick+=rng.randrange(1, 300) 
    
wn=turtle.Screen()
wn.bgcolor("light green")
wn.title("Turtle 2.0")
hec=TurtleGTX()
hec.color("dark green")
hec.shape("turtle")
hec.speed(1)
hec.bk(300)
hec.left(90)
hec.fd(300)
hec.right(135)
hec.fd(100)
wn.mainloop()