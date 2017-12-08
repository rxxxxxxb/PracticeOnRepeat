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

    def isempty(self):
        return self.size == 0    

    def top(self):
        if self.isempty():
            raise Exception('Empty')
        return self.head.element

    def length(self):
        return self.size

    def pop(self):
        pop = self.head.element
        self.head = self.head.next
        self.size =-1
        return pop
    
    def printList(self):
        current = self.head
        count = 0
        while current is not None:
            print(current.element)
            current = current.next
            count += 1
            print(count)
            if count == self.size:
                print("DOne")
                break
            


stack = Stack()         

for r in  range(50):
    rand = random.randint(0,100)
    stack.push(rand)
#stack.push(500)
 
#stack.pop()
l = stack.length()
print("length",l)
# arry = []

# for ran in range(l):# converting linked list to array
#     temp = stack.pop()
#     print("arr : " ,temp)
#     arry.append(temp)
#     print("size " , len(arry))

stack.printList()

# for  r, v  in enumerate(arry):
#     print(r,v)


#     #stack.pop()
#     print(r,v)
#     len = stack.length()
#     top = stack.top()
#     print(top)
#     print(len)
#     stack.pop()