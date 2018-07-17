"ONE"    
def odd_count(col):
    count=0
    for n in col:
        if n%2==1:
            count +=1
        elif n%2==0:
            continue
    return count

"TWO"
def even_sum(xs):
    total=0
    for n in xs:
        if n % 2==0:
            total+=n
        else:
            continue
    return total    

"THREE"
def neg_sum(xs):
    total=0
    for n in xs:
        if n < 0:
            total+=n
        else:
            continue
    return total

"FOUR"
def length_five(xs):
    words=0
    for w in xs:
        if len(w)==5:
            words+=1
        else:
            continue
    return words

"FIVE"
def sum_to_even(xs):
    total=0
    for n in xs:
        if n % 2==0:
            break
        else:
            total+=n
    return total

"SIX"
def to_sam(xs):
    words=0
    for w in xs:
        words+=1
        if w=="sam":
            break
        else:
            continue
    return words

"SEVEN"
def sqrt(n):
    approx = n/2.0 
    while True:
        better = (approx + n/approx)/2.0
        print(better)
        if abs(approx - better) < 0.001:
            return better
        approx = better
        
print(sqrt(25))

"NINE"
def triangular_numbers(n):
    tn=int(n*(n+1)/2)
    return tn
def print_triangular_numbers(n):
    for i in range(1, n+1):
        print(i, "    ", triangular_numbers(i))
        
Q=print_triangular_numbers(6)
print(Q)

"TEN"
def is_prime(n):
    if n >= 2:
        for i in range(2, n):
            if not (n % i):
                return False
    else: 
        return False
    return True

import turtle
"ELEVEN"
xs=[(160, 20), (-43, 10), (270, 8), (-43, 12)]

def draw_path(t):
    for (angle, distance) in xs:
        t.left(angle)
        t.forward(distance)

wn=turtle.Screen()
wn.bgcolor("lightgreen")

Hec=turtle.Turtle()
Hec.shape("turtle")
Hec.color("Green")
Hec.pensize(10)
Hec.speed(1)

draw_path(Hec)

"TWELVE"
xs=[(90, 200), (-135, 200*(2**0.5)), (135, 200), (45, 20000**0.5), (90, 20000**0.5), (135, 200), (-135, 200*(2**0.5)), (135, 200)]

def draw_path(t):
    for (angle, distance) in xs:
        t.left(angle)
        t.forward(distance)

wn=turtle.Screen()
wn.bgcolor("lightgreen")

Hec=turtle.Turtle()
Hec.shape("turtle")
Hec.color("Green")
Hec.pensize(10)
Hec.speed(1)

draw_path(Hec)

wn.mainloop()

"FOURTEEN"
def num_digits(n):
    if n==0:
        count=1
        return count
    else:
        count = 0
        while n != 0:
            count = count + 1
            n = abs(n) // 10
        return count
    
"FIFTEEN"
def num_even_digits(n):
    if n==0:
        digits = 1
        return digits
    else: 
        digits = 0
        while n != 0:
            if n % 2==0:
                digits +=1
                n= abs(n)//10
            else: 
                n=abs(n)//10
        return digits
    
"SIXTEEN"
def sum_of_squares(xs):
    total=0
    for n in xs:
        n= n**2
        total += n
    return total

import random 

"SEVENTEEN"
# Your friend will complete this function
def play_once(hpf):
    if hpf==0:
        print ("Human plays first.")
    elif hpf==1:
        print("Computer plays first.")
    """
       Must play one round of the game. If the parameter
       is True, the human gets to play first, else the
       computer gets to play first.  When the round ends,
       the return value of the function is one of
       -1 (human wins),  0 (game drawn),   1 (computer wins).
    """
    # This is all dummy scaffolding code right at the moment...
                 # See Modules chapter ...
    rng = random.Random()
    # Pick a random result between -1 and 1.
    result = rng.randrange(-1,2)
    print("Human plays first={0},  winner={1} "
                       .format(hpf, result))
    
    return result

draws=0
computer_wins=0
human_wins=0
rng=random.Random()
n = rng.randrange(0, 2)
game_num=0

def play_loop(play):
    global draws
    global computer_wins
    global human_wins 
    global n 
    global game_num
    game_num+=1
    if n==0:
        n=1
    elif n==1:
        n=0
    play_once(n)
    result = rng.randrange(-1,2)
    if result==0: 
        print("Draw.")
        draws+=1
    elif result==1:
        print("Computer wins!")
        computer_wins+=1       
    elif result==-1:
        print("Human wins!")
        human_wins+=1
    if draws==1:
        print("There has been 1 draw.")
    else:
        print("There have been", draws, "draws.")
    if computer_wins==1:
        print("AI has won 1 game.")
    else:
        print("AI has won", computer_wins, "games.")
    if human_wins==1:
        print("Player has won 1 game.")
    else:
        print("Player has won", human_wins, "games.") 
    hpw=human_wins/game_num * 100
    print("Player has won", hpw, "% of the games.")
    play=input("Want to play again? ")
    if play=="yes" or play=="Yes":
        play_loop(1)  
    else:
        print("Goodbye!")   

play_loop(1)


