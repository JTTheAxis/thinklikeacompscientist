"CHAPTER 2"

"ONE"
a="All "
W="work "
N="and "
O="no " 
p="play "
M="makes "
J="Jack "
L="a "
D="dull "
B="boy."
print(a+W+N+O+p+M+J+L+D+B)

"TWO"
print(6*(1-2))

"THREE"
blue=17
print(blue+1)
"Note: After placing a comment before the code, there was a syntax error: invalid syntax: <string>, line 20, pos 12"

"FOUR"
bruce=6
print(bruce + 4)

"FIVE"
P = 10000
r = 0.08
n = 12
t=input("How many years will you be saving money for?")
m=float(t)
A= P*(1+r/n)**n*m
print("You will compound a total of ", A, "dollars.")

"SIX"
print(5%2, 9%5, 15%12, 12%15, 6%6, 0%7)
"Note: 7/0 is an error, leaving no remainder when modulus function is used."

"SEVEN"
CurrentTime=14
TimePassed=51
Alarm=(CurrentTime+TimePassed)%24
print("The Alarm goes off at", Alarm, "o'clock.")

"EIGHT"
TimeNow=input("What is the time now?")
TN=int(TimeNow)
WaitTime=input("How long will you be waiting for?")
WT=int(WaitTime)
AlarmTime=(TN+WT)%24
print("Your alarm will go off at", str(AlarmTime) + ":00.")



