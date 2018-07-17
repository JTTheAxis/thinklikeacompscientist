myfile = open("test.txt", "w")
myfile.write("9 Hours, 9 Persons, 9 Doors\n")
myfile.write("---------------------------------\n")
myfile.write("Seek a way out...seek the door...that carries a '9'. \n")
myfile.write("If he has chosen cards, then I choose dice. Call me Snake.\n")
myfile.write("Just like Rip Van Winkle, out of the ominous coffin Snake rose.")
myfile.close()

"ONE"
def reverse_file(file):
    a=open(file, "r")
    newfile=a.readlines()
    a.close()
    newfile=newfile[::-1]
    rfile=open("reversedfile.txt", "w")
    for line in newfile:
        rfile.write(line)
    rfile.close()
    rfile=open("reversedfile.txt", "r")
    reverse=rfile.read()
    rfile.close()
    print(reverse)
    
#reverse_file("test.txt")

"TWO"
def snake_eyes(file):
    snake=open(file, "r")
    while True:
        cline=snake.readline()
        if len(cline)==0:
            break
        lowerline=cline.lower()
        if "snake" in lowerline:
            print(cline, end="")
        else:
            continue
#snake_eyes("test.txt")

"THREE"
def quaternary(file):
    c1=0
    c2=0
    c3=0
    c4=0
    base=open(file, "r")
    text=base.readlines()
    base.close()
    four=open("numbered.txt", "w")
    for line in text:
        c1=str(c1)
        c2=str(c2)
        c3=str(c3)
        c4=str(c4)
        four.write(c4+c3+c2+c1+" "+line)
        c1=int(c1)
        c2=int(c2)
        c3=int(c3)
        c4=int(c4)
        c1+=1
        if c1==10:
            c1=0
            c2+=1
            if c2==10:
                c2=0
                c3+=1
                if c3==10:
                    c3=0
                    c4+=1
    four.close()
    four=open("numbered.txt", "r")
    num=four.read()
    four.close()
    print(num)
#quaternary("test.txt")

"FOUR"
def denumber_file(file):
    q=open(file, "r")
    u=open("inum.txt", "w")
    while True:
        line=q.readline()
        if len(line)==0:
            break
        if line[0]==int():
            u.write(line[5:])
        else:
            u.write(line)
    q.close()
    u.close()
    u=open("inum.txt", "r")
    plain=u.read()
    u.close()
    print(plain)
#denumber_file("test.txt")