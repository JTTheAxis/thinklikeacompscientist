from unit_tester import *
class MyTime:
    
   def __init__(self, hrs=0, mins=0, secs=0):
      totalsecs = hrs*3600 + mins*60 + secs
      if totalsecs < 0:
         totalsecs= 86400 + totalsecs
      self.hours = totalsecs // 3600        
      leftoversecs = totalsecs % 3600
      self.minutes = leftoversecs // 60
      self.seconds = leftoversecs % 60    
  
   def __str__(self):
      return"{0}, {1}, {2}".format(self.hours, self.minutes, self.seconds)
  
   def increment(self, seconds):
      time=self.to_seconds()+seconds
      return MyTime(0,0,time)
                    
   def to_seconds(self):
      """ Return the number of seconds represented
           by this instance
      """
      return self.hours * 3600 + self.minutes * 60 + self.seconds 
   
   def __eq__(self, target):
      return self.to_seconds==target.to_seconds()
   
   def __gt__(self, target):
      seconds=self.to_seconds()
      time=target.to_seconds()
      if seconds > time:
         return True
      return False   
   
   def __add__(self, other):
      return MyTime(0, 0, self.to_seconds() + other.to_seconds()) 
   
   def between(self, t1, t2):
      seconds1=t1.to_seconds()
      seconds2=t2.to_seconds()
      seconds=self.to_seconds()
      if seconds>=seconds1 and seconds<seconds2:
         return True
      return False     
   
"ONE"
def between(o, t1, t2):
   seconds1=t1.to_seconds()
   seconds2=t2.to_seconds()
   secondso=o.to_seconds()
   if secondso>=seconds1 and secondso<seconds2:
      return True
   return False

time1=MyTime(4, 3, 30)
time2=MyTime(4, 3, 31)
current=MyTime(4, 3, 30)

#print(between(current, time1, time2))
   
"TWO"
##below added as a method to MyTime
def between(self, t1, t2):
   seconds1=t1.to_seconds()
   seconds2=t2.to_seconds()
   seconds=self.to_seconds()
   if seconds>=seconds1 and seconds<seconds2:
      return True
   return False   

#print(current.between(time1, time2))


"THREE"
##below added as a method to MyTime
#def __gt__(self, target):
#   seconds=self.to_seconds()
#   time=target.to_seconds()
#   if seconds > time:
#      return True
#   return False

#print(current > time2)

"FOUR"
##Modification to increment method
#def increment(self, seconds):
#   time=self.to_seconds()+seconds
#   return MyTime(0,0,time)

##Note: Ask Kevin why current is not equal to time1, despite their values being the same. 
