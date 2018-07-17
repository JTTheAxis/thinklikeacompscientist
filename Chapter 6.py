"ONE"
def turn_clockwise(compass):
    North="N"
    East="E"
    South="S"
    West="W"
    if compass==North:
        return "E"
    elif compass==West:
        return "S"
    elif compass== South:
        return "W"
    elif compass== West:
        return "N"

print(turn_clockwise("N"))

"TWO"
def day_name(day):
    Sun= "Sunday"
    Mon="Monday"
    Tues="Tuesday"
    Wed="Wednesday"
    Thurs="Thursday"
    Fri="Friday"
    Sat="Saturday"
    if day==0:
        return Sun
    elif day==1:
        return Mon
    elif day==2:
        return Tues
    elif day==3:
        return Wed
    elif day==4:
        return Thurs
    elif day==5:
        return Fri
    elif day==6:
        return Sat
    
print(day_name(3))

"THREE"
def day_num(name):
    Sun=0
    Mon=1
    Tues=2
    Wed=3
    Thurs=4
    Fri=5
    Sat=6
    if name=="Sunday":
        return Sun
    elif name=="Monday":
        return Mon
    elif name=="Tuesday":
        return Tues
    elif name=="Wednesday":
        return Wed
    elif name=="Thursday":
        return Thurs
    elif name=="Friday":
        return Fri
    elif name=="Saturday":
        return Sat    

print(day_num("Saturday"))

def day_figure(starting_day, delta):
    Sun=0
    Mon=1
    Tues=2
    Wed=3
    Thurs=4
    Fri=5
    Sat=6
    if starting_day=="Sunday":
        starting_day=Sun
    elif starting_day=="Monday":
        starting_day=Mon
    elif starting_day=="Tuesday":
        starting_day=Tues
    elif starting_day=="Wednesday":
        starting_day=Wed
    elif starting_day=="Thursday":
        starting_day=Thurs
    elif starting_day=="Friday":
        starting_day=Fri
    elif starting_day=="Saturday":
        starting_day=Sat       
    final_day=starting_day + delta
    if final_day % 7 == 0:
        print("The target day is a Sunday.")
    elif final_day % 7 == 1:
        print("The target day is a Monday.")  
    elif final_day % 7 == 2:
        print("The target day is a Tuesday.")
    elif final_day % 7 == 3:
        print("The target day is a Wednesday.")  
    elif final_day % 7 == 4:
        print("The target day is a Thursday.")
    elif final_day % 7 == 5:
        print("The target day is a Friday.")            
    elif final_day % 7 == 6:
        print("The target day is a Saturday.")   
              
day_figure("Sunday", -100)

"FIVE"
#Yes, my function can already work with negative deltas due to the fact that negative numbers can still modulus into the proper remainder. 

"SIX"
def days_in_month(month):
    if month=="January":
        return 31
    elif month=="February":
        return 28
    elif month=="March":
        return 31
    elif month=="April":
        return 31    
    elif month=="May":
        return 31    
    elif month=="June":
        return 31    
    elif month=="July":
        return 31    
    elif month=="August":
        return 31    
    elif month=="September":
        return 31    
    elif month=="October":
        return 31    
    elif month=="November":
        return 30
    elif month=="December":
        return 31    
    
print(days_in_month("March"))

"SEVEN"
def to_secs(hrs, mins, secs):
    hrsecs=hrs*60*60
    minsecs=mins*60
    truesecs=secs
    final_secs=hrsecs + minsecs + truesecs 
    return(final_secs)
print(to_secs(2, 30, 10))

"EIGHT"
def to_secs(hrs, mins, secs):
    hrsecs=hrs*60*60
    hrsecs=hrsecs-(hrsecs%1)
    minsecs=round(mins*60)
    minsecs=minsecs-(minsecs%1)
    truesecs=secs - (secs%1)
    final_secs=hrsecs + minsecs + truesecs 
    return(final_secs)

print(to_secs(2.433, 0, 0))

"NINE"
def hours_in(secs):
    round_hrs=secs-secs%3600
    hrs=round_hrs/3600
    return hrs

def minutes_in(secs):
    round_hrs=secs-secs%3600
    hrs=round_hrs/3600    
    round_mins=secs-hrs*3600
    mins=(round_mins-(round_mins%60))/60
    return mins

def seconds_in(secs):
    round_hrs=secs-secs%3600
    hrs=round_hrs/3600    
    round_mins=secs-hrs*3600
    mins=(round_mins-(round_mins%60))/60
    true_secs=secs-mins*60-hrs*3600
    return true_secs

"TEN"
#test(3 % 4 == 0) #fail
#test(3 % 4 == 3) #pass
#test(3 / 4 == 0) #fail
#test(3 // 4 == 0) #pass
#test(3+4  *  2 == 14)#fail
#test(4-2+2 == 0)#fail
#test(len("hello, world!") == 13)#pass

"ELEVEN"
def compare(a, b):
    if a > b:
        return 1
    elif a==b:
        return 0
    else: 
        return -1
print(compare(3,2))

"TWELVE"
def hypotenuse(leg, short):
    square=leg**2 + short**2
    hypot=square**0.5
    return hypot

"THIRTEEN"
def slope(x1, y1, x2, y2):
    rise=y2-y1
    run=x2-x1
    slope=rise/run
    return slope

def intercept(x, y, x1, y1):
    m=slope(x,y,x1,y1)
    b=y-m*x
    return b

"FOURTEEN"
def is_even(n):
    if n % 2==0:
        return True
    else:
        return False
        
"FIFTEEN"
def is_odd(n):
    if is_even(n)==False:
        return True
    else:
        return False
 
"SIXTEEN"
def is_factor(f, n):
    if n % f == 0:
        return True
    else: 
        return False
    
"SEVENTEEN"
def is_multiple(m, n):
    if is_factor(n, m)==True:
        return True
    else: 
        return False
    
"EIGHTEEN"
def f2c(t):
    celsius=(t-32)/1.8
    true_celsius=round(celsius)
    return true_celsius 

"NINETEEN"
def c2f(t):
    heit=(t*1.8) + 32
    true_heit=round(heit)
    return true_heit       