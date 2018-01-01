class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next

    def _getData(self):
        return self.data

class LinkedList:
    def __init__(self,head = None):
        self.head = None

    def input(self,data):
        node = Node(data,self.head)            


        self.head = node

    def showLL(self):
        size = 0
        CurrentNode = self.head
        while CurrentNode is not None:
            print("all, ",CurrentNode.data)  
            CurrentNode = CurrentNode.next  
            size +=1
        print(size)    

ll = LinkedList()        

ll.input(50)
ll.input(500)
ll.input(50000)

ll.showLL()