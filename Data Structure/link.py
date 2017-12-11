import random

class LinkedList:
    def __init__(self):
        self.head = 0
        self.size = 0

    class Node:
        def __init__(self,element,next=None ):
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

    def COnvertToArray(self):
        self.arry = []
        for ran in range(l):  # converting linked list to array
            temp = self.pop()
            self.arry.append(temp)
            #print("Index :", len(self.arry), "and Value : ", temp)
        return self.arry    

    def PrintArray(self):
        for r, v in enumerate(self.arry,1):
            print(r,v)

    def FindData(self,Data):
        current = self.head
        print("Search : " ,Data)
        
        while current is not None:
            print(current.element)
            if current.element == Data:
                print("Data :", Data ," = element :",current.element)               
                return 0
            current = current.next
        return ("Not found")
        
            
stack = LinkedList()         

# for r in  range(10):
#     rand = random.randint(0,1)
#     stack.push(rand)

stack.push(1)
stack.push(2)
stack.push(3)

stack.push(4)
#stack.pop()

l = stack.length()
print("length",l)

stack.FindData(9)


# stack.COnvertToArray()
# stack.PrintArray()

#stack.printList()

