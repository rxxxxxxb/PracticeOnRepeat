class Node:
    def __init__(self,value,next):
        self.value = value
        self.next = next

    def _value(self):
        return self.value    

class LinkedList:
    def __init__(self):
        self.head = None    

    def insert(self,data):
        node = Node(data,self.head)

        self.head = node

    def printAll(self):
        CurrentNode = self.head
        size = 0
        while CurrentNode is not None:
            print('node',CurrentNode.value)
            CurrentNode = CurrentNode.next
            size += 1 
        print(size)    


ll = LinkedList()

ll.insert(10)            
ll.insert(1)
ll.insert(10000)

ll.printAll()
