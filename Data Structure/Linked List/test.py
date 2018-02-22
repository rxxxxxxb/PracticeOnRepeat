class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next
        
class List:
    def __init__(self,head = None):
        self.head = head

    def insert(self,data):
        node = Node(data,self.head)
        self.head = node

    def PrintAll(self):
        currentNode = self.head
        size = 0

        while currentNode is not None:
            p = currentNode.data
            print(p)
            size += 1 
            currentNode = currentNode.next

        print("Size of the list :",size)        


link = List()

link.insert(92)
link.insert(9)
link.insert(452)
link.insert(9484774)                    

link.PrintAll()
