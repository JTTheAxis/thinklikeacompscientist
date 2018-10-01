class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

"ONE"    
def print_tree_inorder(tree):
    if tree is None: return
    #if tree.left and if tree.right test if the next branch is None or not: if it's None, it returns False, otherwise it returns True. 
    if tree.left:
        print("(", end=" ")
    print_tree_inorder(tree.left)
    print(tree.cargo, end=" ")
    print_tree_inorder(tree.right)
    if tree.right:
        print(")", end=" ")    
    
        
exp=Tree("+", Tree(1), Tree("*", Tree(2), Tree(3)))
#print_tree_inorder(exp)
#The pairs of parentheses are always clear and unambiguous as to which operations should be performed first.
#However, they are most certainly not necessary. There will always be a pair of parentheses enclosing the final pair of operands, which is unnecessary as there is only one operation left to be performed. This is excluding, of course, the fact that without parentheses, multiplication always happens before addition anyways.

"TWO"
def transform_token(expr):
    list=[]
    num=""
    for x, char in enumerate(expr):
        #if char is empty space, keep going.
        if char==" ":
            continue
        #if char is a digit/number, append the respective integer.
        elif char.isdigit():
            list.append(int(char))
        #if char is not a number, add it directly to the list.
        else:
            list.append(char)
    #add end to the token list so that it knows when to end. 
    list.append("end")
    return list

m="578 + ( 9 + 7 ) * 31"
print(transform_token(m))

"THREE"
def get_token(token_list, expected):
    if len(token_list)==0:
        #If end is not put at the end of the statement, raise an error. 
        raise IndexError("Incomplete Expression")
    if token_list[0] == expected:
        token_list.append(token_list[0])
        del token_list[0]
        return True
    return False

def get_number(token_list):
    if get_token(token_list, "("):
        x=get_sum(token_list)
        if not get_token(token_list, ")"):
            raise ValueError("Missing close parenthesis")
        return x
    else:
        x = token_list[0]
        if type(x) != type(0): return None
        token_list.append(token_list[0])
        del token_list[0]
        return Tree(x, None, None)

def get_product(token_list):
    a = get_number(token_list)
    if a==None:
        #raise error if two non-numbers are adjacent
        raise ValueError("Two non-numbers should not be beside each other.")
    if type(token_list[0])==type(0):
        #raise error if two numbers are adjacent
        raise ValueError("Two operands should not be beside each other.")
    if get_token(token_list, "*"):
        b = get_product(token_list) #originally b=get_number(token_list)
        return Tree("*", a, b)
    return a

def get_sum(token_list):
    if not str(token_list[0]).isdigit():
        #raise error if expression does not start with a number
        raise ValueError("Expressions must begin with a number.")
    if token_list.count(")") > token_list.count("(") or token_list.count(")") < token_list.count("(") :
        #if there are not enough open braces to match closing braces:
        raise ValueError("Not enough matching braces.")
    a = get_product(token_list)
    if get_token(token_list, "+"):
        b = get_product(token_list)
        return Tree("+", a, b)
    return a

def print_tree_postorder(tree):
    if tree is None: return
    print_tree_postorder(tree.left)
    print_tree_postorder(tree.right)
    print(tree.cargo, end=" ")
    
exp=[1 , "+", 3, "*", 5, "end"]
tree=get_sum(exp)
print_tree_postorder(tree)

"FOUR"
def yes(ques):
    ans = input(ques).lower()
    return ans[0] == "y"

def animal():
    # Start with a singleton
    root = Tree("bird")
    #Recall previously imprinted information. 
    tree=recall(root, "animalinfo.txt")
    # Loop until the user quits
    while True:
        print()
        if not yes("Are you thinking of an animal? "): break

        # Walk the tree
        tree = root
        path=[]
        while tree.left is not None:
            prompt = tree.cargo + "? "
            if yes(prompt):
                tree = tree.right
                path.append("yes")
            else:
                tree = tree.left
                path.append("no")
        # Make a guess
        guess = tree.cargo
        prompt = "Is it a " + guess + "? "
        if yes(prompt):
            print("I rule!")
            continue

        # Get new information
        prompt  = "What is the animal's name? "
        animal  = input(prompt)
        prompt  = "What question would distinguish a {0} from a {1}? "
        question = input(prompt.format(animal, guess))

        # Add new information to the tree
        tree.cargo = question
        prompt = "If the animal were {0} the answer would be? "
        if yes(prompt.format(animal)):
            tree.left = Tree(guess)
            tree.right = Tree(animal)
            imprint(path, "yes", question, guess, animal)
        else:
            tree.left = Tree(animal)
            tree.right = Tree(guess)
            imprint(path, "no", question, guess, animal)
        
#imprints each round of updated information into a file in the correct order.  
def imprint(path, answer, question, guess, animal):
    #open a file called animalinfo.txt
    ai=open("animalinfo.txt", "a")
    #use an accumulator to transform the path taken into a string. 
    string_path=""
    for prompt in path:
        string_path+=prompt+" "
    ai.write(string_path+"\n")
    ai.write(answer+"\n")
    ai.write(question+"\n")
    #essentially, if the answer is yes, write the guess first (on the left of the tree) and the new animal second (on the right of the tree). Otherwise, do the same thing but in the reverse order. 
    if answer[0]=="y":
        ai.write(guess+"\n")
        ai.write(animal+"\n")
    else:
        ai.write(animal+"\n")
        ai.write(guess+"\n")
    ai.close()

#recall all previously obtained information whenever the animal() function is called.     
def recall(root, file):
    #set tree equal to the same root as before. 
    tree=root
    #count for which path is currently being retraced.
    pathcount=0
    #count which term is being added to the tree.
    termcount=0    
    ai=open(file, "r")
    contents=ai.readlines()
    if len(contents)==0:
        return root
    paths=[]
    answers=[]
    questions=[]
    guesses=[]
    animals=[]
    while True:
        if len(contents)==0:
            break
        prompts=contents[0].split()
        paths.append(prompts)
        del contents[0]
        answers.append(contents[0][:len(contents[0])-1])
        if contents[0][0]=="y":
            #when appending, cut off the newline characters.
            del contents[0]
            questions.append(contents[0][:len(contents[0])-1])
            del contents[0]
            guesses.append(contents[0][:len(contents[0])-1])
            del contents[0]
            animals.append(contents[0][:len(contents[0])-1])
            del contents[0]
        else:
            del contents[0]
            questions.append(contents[0][:len(contents[0])-1])
            del contents[0]
            animals.append(contents[0][:len(contents[0])-1])
            del contents[0]
            guesses.append(contents[0][:len(contents[0])-1])
            del contents[0]  
    while True:
        #set lettercount, a variable that determines the direction of the path, every iteration of the loop
        lettercount=0
        while tree.left is not None:
            if paths[pathcount]==[]:
                break
            if paths[pathcount][lettercount][0]=="y":
                tree=tree.right
            else:
                tree=tree.left
            lettercount+=1
        tree.cargo=questions[termcount]
        if answers[termcount][0]=="y":
            tree.left=Tree(guesses[termcount])
            tree.right=Tree(animals[termcount])
        else:
            tree.left=Tree(animals[termcount])
            tree.right=Tree(guesses[termcount])
        tree=root
        if pathcount==len(paths)-1:
            break
        #when finished with the current path, add 1 to pathcount to traverse the next list in paths the next time
        pathcount+=1
        #add 1 to termcount so as to add the next set of terms to the tree.
        termcount+=1
    ai.close()
    return tree