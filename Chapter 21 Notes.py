class MyTime:

#    def __init__(self, hrs=0, mins=0, secs=0):
#        """ Create a MyTime object initialized to hrs, mins, secs """
#        self.hours = hrs
#        self.minutes = mins
#        self.seconds = secs
    
    
    ##More powerful initializer that immediately normalizes the time, or splits it into the proper hours, minutes and seconds.
   def __init__(self, hrs=0, mins=0, secs=0):
      """ Create a new MyTime object initialized to hrs, mins, secs.
         The values of mins and secs may be outside the range 0-59,
         but the resulting MyTime object will be normalized.
      """

       # Calculate total seconds to represent
      totalsecs = hrs*3600 + mins*60 + secs
      self.hours = totalsecs // 3600        # Split in h, m, s
      leftoversecs = totalsecs % 3600
      self.minutes = leftoversecs // 60
      self.seconds = leftoversecs % 60    
        ##Increment as a method.    
   def increment(self, seconds):
      self.seconds += seconds

      while self.seconds >= 60:
         self.seconds -= 60
         self.minutes += 1

      while self.minutes >= 60:
         self.minutes -= 60
         self.hours += 1    
            
    ##Key insight that any MyTime object is a 3 digit number in base 60, which is why we carry 60 minutes and seconds over to the next "column". In this case, we can add the total number of seconds represented by the hours, minutes and seconds in order to find the value of the object in seconds.         
   def to_seconds(self):
      """ Return the number of seconds represented
           by this instance
      """
      return self.hours * 3600 + self.minutes * 60 + self.seconds 
     
     ##After method which compares if the current time (the time invoking the method) is after the target time.
   def after(self, time2):
      """ Return True if I am strictly greater than time2 """
      if self.hours > time2.hours:
         return True
      if self.hours < time2.hours:
         return False
      if self.minutes > time2.minutes:
         return True
      if self.minutes < time2.minutes:
         return False
      if self.seconds > time2.seconds:
         return True
      return False     
     
    ##Refined after function utilizing the fact that all time is in base 60. 
   def after(self, time2):
      """ Return True if I am strictly greater than time2 """
      return self.to_seconds() > time2.to_seconds()   
     
    ##Add method that adds the values of two times, returning a new MyTime object representing the sum of the two objects. By doing so, we overwrite the built in addition function, which is represented by "+".
   def __add__(self, other):
      return MyTime(0, 0, self.to_seconds() + other.to_seconds())     
tim1=MyTime(11, 59, 30)

def add_time(t1, t2):
   h = t1.hours + t2.hours
   m = t1.minutes + t2.minutes
   s = t1.seconds + t2.seconds
   sum_t = MyTime(h, m, s)
   return sum_t

##Modified version of add_time to accommodate for minutes and seconds that go over 60.
def add_time(t1, t2):

   h = t1.hours + t2.hours
   m = t1.minutes + t2.minutes
   s = t1.seconds + t2.seconds

   if s >= 60:
      s -= 60
      m += 1

   if m >= 60:
      m -= 60
      h += 1

   sum_t = MyTime(h, m, s)
   return sum_t

##Draft of the "modifier" version of add_time
def increment(t, secs):
   t.seconds += secs

   if t.seconds >= 60:
      t.seconds -= 60
      t.minutes += 1

   if t.minutes >= 60:
      t.minutes -= 60
      t.hours += 1

##Increment but with while loops to make sure that the number of minutes will not be over 60, as in the previous version, the if statement would only carry 60 minutes once, meaning that the number of minutes could be over 60. (Ex. 121 mins. If minutes >60, minutes+=-60, but 121-60=61, which is still more than a possible number of minutes.)         
def increment(t, seconds):
   t.seconds += seconds

   while t.seconds >= 60:
      t.seconds -= 60
      t.minutes += 1

   while t.minutes >= 60:
      t.minutes -= 60
      t.hours += 1


##Rewritten version of add_time using the advantage of the new initializer.        
def add_time(t1, t2):
   secs = t1.to_seconds() + t2.to_seconds()
   return MyTime(0, 0, secs)

##Front and back makes a copy of the list, reverses it, and concatenates the two together. 
def front_and_back(front):
   import copy
   back = copy.copy(front)
   back.reverse()
   print(str(front) + str(back)) 
#Duck Typing Rule: If all of the operations inside of a function can be applied to the type, thefunction can be applied to the type. Originates from the duck test: "if it walks like a duck and quacks like a duck, it must be a duck."

