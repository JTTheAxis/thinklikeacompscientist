class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next  = next

    def __str__(self):
        return str(self.cargo)
    
    def print_backward(self):
        if self.next is not None:
            tail = self.next
            tail.print_backward()
        print(self.cargo, end=" ")
        
    def print_list(self):
        if self.next is None:
            print(self, end="]")
        else:
            print(self, end=", ")
            self.next.print_list() 
            
"ONE"
class ListQueue:
    def __init__(self):
        self.items=[]
        
    def is_empty(self):
        return self.items==[]
    
    def insert(self, cargo):
        self.items.append(cargo)
        
    def remove(self, cargo):
        #return none if the list is empty
        if self.is_empty():
            return None
        first=self.items[0]
        self.items.remove(first)
        return first
    
q=ListQueue()
for i in range(1, 1000):
    q.insert(i)
print(q.items)

while not q.is_empty():
    print(q.remove(i))
    
"TWO"
class PriorityLinked:
    def __init__(self):
        self.length=0
        self.head=None
        
    def is_empty(self):
        return self.length==0
    
    #version of insert that enables remove to be linear time
    def insert(self, cargo):
        node=Node(cargo)
        if self.head is None:
            self.head=node
        #if the new node is bigger than the current first node, put it in the front instead. This keeps the linked list sorted from largest to smallest.
        elif cargo > self.head.cargo:
            node.next=self.head
            self.head=node
        #if the new node is not bigger than the current first node, create a loop that traverses the list until it either finds a node smaller than the new node, or reaches the end of the list.
        else:
            #set a variable to contain the node that should be smaller than the new node
            n1=self.head
            while n1.cargo>=cargo:
                #n2 is the node that will be before the new node; in other words, the new node will be put between n2 and n1.
                n2=n1
                n1=n1.next
                #break if the end of the linked list is reached
                if n1==None:
                    break
            #set the new node between n1 and n2
            node.next=n1
            n2.next=node
        self.length+=1
                  
    def remove(self):
        if self.is_empty():
            return None
        max=self.head.cargo
        #set the current first term equal to the term right after it, the priority of which node should be removed first is taken care of as the list is sorted by insert already.
        self.head=self.head.next
        self.length-=1
        return max

q=PriorityLinked()
for i in range(1, 10):
    q.insert(i)
import random
rng=random.Random()
print(q.remove())
print(q.remove())
