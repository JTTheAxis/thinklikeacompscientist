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
    
class SMS_store:
    
    
    def __init__(self):
        self.l = []
        
       
    def __str__(self):
        return("{0}".format(self.l))
     
        
    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        inbox=self.l
        msg=(from_number, time_arrived, text_of_SMS)
        msg=msg+(False,)
        inbox.append(msg)
        return inbox
    

    def message_count(self):
        length=len(self.l)
        return length    
    
    
    def get_unread_indices(self):
        inbox=self.l
        unread=[]
        for i, msg in enumerate(inbox):
            if msg[3]==False:
                unread.append(i)
        return unread   
    
    
    def get_message(self, i):
        inbox=self.l
        cmsg=inbox[i]
        cmsg=cmsg[:3] + ("has been viewed.",)
        return cmsg    
    
    
    def delete(self, i):
        inbox=self.l
        del inbox[i]
        return inbox 
    
    
    def clear(self):
        self.l=[]
        return self.l    
# Other statements outside the class continue below here.

"ONE"
def distance(p1, p2):
    dx = p2.x-p1.x
    dy = p2.y-p1.y
    distance=(dx**2+dy**2)**0.5
    return distance

p=Point(3,6)
q=Point(5,4)
r=Point(4,5)
s=Point(2,3)

#print(distance(p, q))
#test(distance(p, q)==5.0)

"TWO"
#def reflect_x(self):
#    nx=self.x
#    ny=self.y * -1
#    return Point(nx, ny)
##Above added to the Point class.

#print(p.reflect_x())
#print(q.reflect_x())

"THREE"
#def slope_from_origin(self):
#    slope=self.y/self.x
#    return slope
##Above added as method to Point class
#print(p.slope_from_origin())
#print(q.slope_from_origin())
##The method slope_from_origin fails whenever the point using the method has a x-coordinate of zero, or is on the y-axis. This is because the origin's x and y-values are both 0, so they do not affect the calculation of the point's slope. In essence, the slope_from_origin function simply divides the point's y coordinate by their x coordinate, which is undefined if the x-coordinate is zero, as one cannot divide by zero. 

"FOUR"
#def line_equation(self, second):
#    rise=second.y-self.y
#    run=second.x-self.x
#    slope=rise/run
#    y=self.y
#    x=self.x
#    m=slope
#    b=y-m*x
#    return(m, b)
##Above added to Point class    
#print(Point(4, 11).line_equation(Point(6, 15)))

"FIVE"
def center(p1, p2, p3, p4):
    line1=p1.line_equation(p2)
    d1=Point((p1.x+p2.x)/2,(p1.y+p2.y)/2)
    m1=-(line1[0]**-1)
    b1=d1.y-m1*d1.x
    line2=p1.line_equation(p3)
    d2=Point((p1.x+p3.x)/2, (p1.y+p3.y)/2)
    m2=-(line2[0]**-1)
    b2=d2.y-m2*d2.x
    cx=(b2-b1)/(m1-m2)
    cy=m1*cx+b1
    center=Point(cx, cy)
    return center

#print(center(p,q,s,r))
##The center function will fail when the slopes of the 2 perpendicular bisectors being calculated is the same, or in any situation when line_equation fails, which would be if the x-coordinates of the two points are equal. 

"SIX"
my_inbox=SMS_store()
#def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
    #inbox=self.l
    #msg=(from_number, time_arrived, text_of_SMS)
    #inbox.append(msg)
    #return inbox
##add_new_arrival method
my_inbox.add_new_arrival("647-519-2609", "06:30", "Hi, is this Frank?")
my_inbox.add_new_arrival("905-819-0522", "09:30", "When are you getting home?")
#print(my_inbox)


#def message_count(self):
    #length=len(self.l)
    #return length
##message_count method
#count=my_inbox.message_count()
#test(count==3)

#def get_unread_indices(self):
#    inbox=self.l
#    unread=[]
#    for i, msg in enumerate(inbox):
#        if msg[3]==False:
#            unread.append(i)
#    return unread
##unread_indices method

new=my_inbox.get_unread_indices()         
#print(new)    

#def get_message(self, i):
#    inbox=self.i
#    cmsg=inbox[i]
#    cmsg=cmsg[:3] + ("has been viewed.")
#    return cmsg
##message retrieval

first=my_inbox.get_message(0)
#print(first)

#def delete(self, i):
#    inbox=self.l
#    inbox[i]=None
#    return inbox
##message delete
#my_inbox.delete(0)
#print(my_inbox)

#def clear(self):
#   self.l=[]
#   return self.l
##Clearing inbox
#my_inbox.clear()
#print(my_inbox)
