import random

class Stack:
    def __init__(self):
        self.head = 0
        self.size = 0

    class Node:
        def __init__(self,element,next):
            self.element = element    
            self.next = next            
  
    def push(self,e):
        self.head = self.Node(e,self.head)
        self.size += 1

    def top(self):
        return self.head.element

    def length(self):
        return self.size

stack = Stack()         

for r in  range(100):
    rand = random.randint(0,r)
    stack.push(rand)
#stack.push(500)

len = stack.length()
top = stack.top()
print(top)
print(len)
