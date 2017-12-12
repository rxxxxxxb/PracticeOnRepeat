class Node:
    def __init__(self,element,next):
        self.element = element
        self.next = next

class LinkedStack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self,e):    
        self.head = Node(e,self.head)
        self.size += 1

    def top(self):
        return self.head.element

    def pop(self):
        pop = self.head.element
        self.head = self.head.next
        self.size =-1
        return pop

link = LinkedStack()    

link.push(10)
print(link.top())