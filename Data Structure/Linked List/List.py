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
        self.head = node
        return node 

    def size(self):
        current = self.head
        counter = 0
        while current is not None:
            counter += 1
            current = current.next
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

link.insert(500)
link.insert(590)
link.insert(40)    

link.size()
link.printAll()