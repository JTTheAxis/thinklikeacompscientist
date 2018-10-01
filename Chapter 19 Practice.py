"ONE"
def readposint():
    n=input("Enter a positive integer: ")
    if str(n)=="":
        print("No input detected.")  
        return
    try:
        n=int(n)
    except:
        print("{0} is not an integer.".format(n))    
        return
    if n < 0:
        print("{0} is not positive.".format(n))
        return
    else:
        print(n)
        
readposint()
        
    