from unit_tester import *
class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y
        
    def __str__(self):
        return("{0}, {1}".format(self.x, self.y))
    
    def reflect_x(self):
        nx=self.x
        ny=self.y * -1
        return Point(nx, ny)
    
    def slope_from_origin(self):
        slope=self.y/self.x
        return slope    
    
    def line_equation(self, second):
        rise=second.y-self.y
        run=second.x-self.x
        m=rise/run
        y=self.y
        x=self.x
        b=y-m*x
        m=int(m)
        b=int(b)
        return(m, b)   
    
class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return  "({0}, {1}, {2})".format(self.corner, self.width, self.height)
    
    def area(self):
        width=self.width
        height=self.height
        area=width*height
        return area    
    
    def perimeter(self):
        width=self.width
        height=self.height
        perimeter=2*(width+height)
        return perimeter    
    
    def flip(self):
        (self.width, self.height)=(self.height, self.width)
        return self   
    
    def contains(self, point):
        x=point.x
        y=point.y
        bx=self.corner.x
        ex=self.corner.x+self.width
        by=self.corner.y
        ey=self.corner.y+self.height
        if x >= bx and x < ex and y >= by and y < ey:
            return True
        else:
            return False    
        
    def collision(self, point):
        x=point.x
        y=point.y
        bx=self.corner.x
        ex=self.corner.x+self.width
        by=self.corner.y
        ey=self.corner.y+self.height
        if x >= bx and x <= ex and y >= by and y <= ey:
            return True
        else:
            return False    
box = Rectangle(Point(0, 0), 100, 200)
bomb = Rectangle(Point(100, 80), 5, 10)    # In my video game
#print("box: ", box)
#print("bomb: ", bomb)

"ONE"
#def area(self):
#    width=self.width
#    height=self.height
#    area=width*height
#    return area
##Area method
r=Rectangle(Point(0,0), 10, 5)
#test(r.area()==50)

"TWO"
#def perimeter(self):
#    width=self.width
#    height=self.height
#    perimeter=2(width+height)
#    return perimeter
##Perimeter method

#test(r.perimeter()==30)

"THREE"
#def flip(self):
#    (self.width, self.height)=(self.height, self.width)
#    return self 
##Swap width and height, thus rotating the rectangle by 90 degrees around its center. 

#r = Rectangle(Point(100, 50), 10, 5)
#test(r.width == 10 and r.height == 5)
#r.flip()
#test(r.width == 5 and r.height == 10)

"FOUR"
#def contains(self, point):
#    x=point.x
#    y=point.y
#    bx=self.corner.x
#    ex=self.corner.x+self.width
#    by=self.corner.y
#    ey=self.corner.y+self.height
#    if x >= bx and x < ex and y >= by and y < ey:
#        return True
#    else:
#        return False
##Check if a point is in a rectangle.

r = Rectangle(Point(0, 0), 10, 5)
test(r.contains(Point(0, 0)))
test(r.contains(Point(3, 3)))
test(not r.contains(Point(3, 7)))
test(not r.contains(Point(3, 5)))
test(r.contains(Point(3, 4.99999)))
test(not r.contains(Point(-3, -3)))

"FIVE"
def collision(a, b):
    ax=a.corner.x
    ay=a.corner.y
    ah=a.height
    aw=a.width
    bx=b.corner.x
    by=b.corner.y
    bh=b.height
    bw=b.width
    #Set the 4 points of the first rectangle
    a1=Point(ax, ay) 
    a2=Point(ax+aw, ay)
    a3=Point(ax, ay+ah)
    a4=Point(ax+aw, ay+ah)
    #Check if each point collides or is indside the second rectangle
    if b.collision(a1)==True:
        return True
    elif b.collosion(a2)==True:
        return True
    elif b.collision(a3)==True:
        return True
    elif b.collision(a4)==True:
        return True
    else:
        return False
    
##Collision testing function
    
    
    