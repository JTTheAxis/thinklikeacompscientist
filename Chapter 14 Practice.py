from unit_tester import *
"ONE"
a=[1,2,3,4,5]
b=[3,4,5,6]

##1a
def mergeA(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):
            for i in ys[yi:]:
                if i in xs:
                    result.append(i)
            return result          

        if yi >= len(ys):
            for i in xs[xi:]:
                if i in ys:
                    result.append(i)
            return result

        if xs[xi] <= ys[yi]:
            if xs[xi] in ys:
                result.append(xs[xi])
            xi += 1
        else:
            if ys[yi] in xs:
                result.append(ys[yi])
            yi += 1
            
#print(mergeA(a, b))

##1b
def mergeB(xs, ys):
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):
            return result          

        if yi >= len(ys):
            result.extend(xs[xi:])
            return result

        if xs[xi] <= ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            if ys[yi] in xs:
                result.append(ys[yi])
            yi += 1
#print(mergeB(a, b))

##1c
def mergeC(xs, ys):
    result = []
    xi = 0
    yi = 0

    while True:
        if yi >= len(ys):
            return result          

        if xi >= len(xs):
            result.extend(ys[yi:])
            return result

        if ys[yi] <= xs[xi]:
            result.append(xs[xi])
            yi += 1
        else:
            if xs[xi] in ys:
                result.append(xs[xi])
            xi += 1
#print(mergeC(a, b))

##1d
def mergeD(xs, ys):
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):          # If xs list is finished,
            result.extend(ys[yi:]) # Add remaining items from ys
            return result          # And we're done.

        if yi >= len(ys):          # Same again, but swap roles
            result.extend(xs[xi:])
            return result

        # Both lists still have items, copy smaller item to result.
        if xs[xi] <= ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            result.append(ys[yi])
            yi += 1
#print(mergeD(a, b))

#1e
def bagdiff(xs, ys):
    result=xs
    sec=ys
    ri=0
    si=0
    while True:
        if ri>=len(result):
            break
        val=result[ri]
        ri+=1
        if val in sec:
            result.remove(val)
            sec.remove(val)
            ri+=-1

    return result

#print(bagdiff([5,7,11,11,11,12,13], [7,8,11]))

def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0)        # Calc the absolute y distance
    dx = abs(x1 - x0)        # CXalc the absolute x distance
    return dx == dy  

def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
         with any queen to its left.
    """
    for i in range(c):     # Look at all columns to the left of c
          if share_diagonal(i, bs[i], c, bs[c]):
              return True

    return False      

def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
        We're assuming here that the_board is a permutation of column
        numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1,len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False

"TWO"
def queens():
    import random
    import time
    rng = random.Random()   # Instantiate a generator

    bd = list(range(15))     # Generate the initial permutation
    num_found = 0
    tries = 0
    te=0
    while num_found < 10:
        tc=time.clock()
        rng.shuffle(bd)
        tries += 1
        if not has_clashes(bd):
            print("Found solution {0} in {1:4f} seconds.".format(bd, tc-te))
            te=time.clock()
            tries = 0
            num_found += 1

#queens()
#The largest board that can be consistently solved within a minute by the Queens program is a 15x15 board. 

"THREE"
def Queensnr():
    import random
    rng = random.Random()   # Instantiate a generator
    solutions=[]
    bd = list(range(8))     # Generate the initial permutation
    num_found = 0
    tries = 0
    while num_found < 10:
        rng.shuffle(bd)
        tries += 1
        if not has_clashes(bd) and bd not in solutions:
            print("Found solution {0} in {1} tries.".format(bd, tries))
            solutions+=bd
            tries = 0
            num_found += 1

Queensnr()

"FOUR"
board=[0,4,7,5,2,6,1,3]
sb=[0,1,2,3]
##4a
def reverseY(bd):
    bdy=[]
    for i in bd:
        bdy.append(i)
    bdy.reverse()
    return bdy
#print(reverseY(board))

##4b
def reverseX(bd):
    bdx=[]
    for x in bd:
        bdx.append(len(bd)-(x+1))
    return bdx

#print(reverseX(board))
        
##4c
def rotate90(bd):
    rbd=[]
    length=len(bd)-1
    for i in range(len(bd)):
        rbd.append(-1)
    for x, y in enumerate(bd):
        rbd[y]=length-x
    return rbd

#print(rotate90(board))

def rotate180(bd):
    rbd=reverseX(bd)
    rbd=reverseY(rbd)
    return rbd

#print(rotate180(board))

def rotate270(bd):
    rbd=rotate90(bd)
    rbd=rotate180(rbd)
    return rbd

#print(rotate270(sb))

##4d
def sym(bd):
    fam=[]
    fam.append(bd)
    nbd=rotate90(bd)
    fam.append(nbd)
    nbd=rotate180(bd)
    fam.append(nbd)
    nbd=rotate270(bd)
    fam.append(nbd)
    nbd=reverseX(bd)
    fam.append(nbd)
    nbd=reverseY(bd)
    fam.append(nbd)
    nbd=rotate90(reverseX(bd))
    fam.append(nbd)
    nbd=rotate90(reverseY(bd))
    fam.append(nbd)
    return fam

#print(sym(board))

##4e
def Queensws(num):
    import random
    rng = random.Random()   # Instantiate a generator
    solutions=[]
    bd = list(range(num))     # Generate the initial permutation
    num_found = 0
    tries = 0
    while num_found < 12:
        rng.shuffle(bd)
        tries += 1
        if not has_clashes(bd) and bd not in solutions:
            print("Found solution {0} in {1} tries.".format(bd, tries))
            fam=sym(bd)
            for sb in fam:
                solutions.append(sb)
            tries = 0
            
#Queensws(8)

"FIVE"
my_tickets = [ [ 7, 17, 37, 19, 23, 43],
               [ 7,  2, 13, 41, 31, 43],
               [ 2,  5,  7, 11, 13, 17],
               [13, 17, 37, 19, 23, 43] ]

def is_prime(n):
    if n >= 2:
        for i in range(2, n):
            if not (n % i):
                return False
    else: 
        return False
    return True

##5a
def lotto_draw():
    import random
    rng=random.Random()
    draw=list(range(1, 49))
    rng.shuffle(draw)
    draw=draw[0:6]
    return draw

#print(lotto_draw())

##5b
def lotto_match(d, t):
    cc=0
    for n in t:
        if n in d:
            cc+=1
    return cc

#test(lotto_match([42,4,7,11,1,13], [2,5,7,11,13,17]) == 3)

##5c
def lotto_list(d, l):
    matches=[]
    for t in l:
        m=lotto_match(d, t)
        matches.append(m)
    return matches

#test(lotto_list([42,4,7,11,1,13], my_tickets) == [1,2,3,1])

##5d
def primes_in(l):
    count=0
    for n in l:
        if is_prime(n):
            count+=1
    return count

#test(primes_in([42, 4, 7, 11, 1, 13]) == 3)


##5f
def repeat_lotto(l, n):
    tries=0
    count=0
    trylist=[]
    cgs=[]
    while True:
        draw=lotto_draw()
        while n not in cgs:
            tries+=1
            cgs=lotto_list(draw, l)
            draw=lotto_draw()
        trylist.append(tries) ##Adds the current number of tries to our list
        count+=1
        print("!", end="") ##Progress bar
        if count >=20:
            print("", end="\n") ##Adds line break so that the result is printed on a new line
            break
        cgs=[]
        tries=0
    average=sum(trylist)/len(trylist) ##Calculates average of our results
    return average
            
print(repeat_lotto(my_tickets, 5)) 
##For three correct picks, around an average of 16 draws is needed.
##For four correct picks, around an average of 200 draws is needed.
##For five correct picks, around an average of 16000 draws is needed.