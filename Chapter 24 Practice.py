class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        
    def print_backward(self):
        print("[", end=" ")
        if self.head is not None:
            self.head.print_backward()
    
    def add_first(self, cargo):
        node = Node(cargo)
        node.next = self.head
        self.head = node
        self.length += 1   
    
    def print_list(self):
        print("[", end="")
        if self.head is not None:
            print(self.head, end=", ")
            self.head.next.print_list()
                
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
        
        
l=LinkedList()
l.head=Node(0)
node1=Node(1)
node2=Node(2)
node3=Node(3)
l.head.next=node1
node1.next=node2
node2.next=node3

l.print_list()

