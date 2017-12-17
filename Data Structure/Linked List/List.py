import random

class Node:
    def __init__(self,data,next):
        self.next = next
        self.data = data

    def __str__(self):
        return self.data

class LinkedList:
    def __init__(self,head = None):
        self.head = head

    def insert(self,data):
        node = Node(data, self.head)
        p = node.__str__()
        print(p)
        self.head = node
        return node 

    def size(self):
        currentNode = self.head
        counter = 0
        while currentNode is not None:
            counter += 1
            currentNode = currentNode.next
        print(counter)    
   

    def printAll(self):
        data = []      
        current = self.head
        while current is not None:
            data.append(current.data)
            current = current.next
        
        print(data)       
        for i in data:
            print(i)    
 


link = LinkedList()

for ran in range(1):
    rand = random.randint(0,50)
    link.insert(rand) 

link.size()
#print("SIze of list ",l)
#link.printAll()

