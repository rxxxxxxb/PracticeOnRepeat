class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next

class Link:
    def __init__(self,head = None):
        self.head = head

    def insert(self,data):
        node = Node(data,self.head)

        self.head = node            

    def PrintAll(self):
        currentNode = self.head
        size = 0

        while currentNode is not None:
            current = currentNode.data
            print(current)
            size += 1 
            currentNode = currentNode.next

        print("Size of the list :",size)       


list = Link()

list.insert(12)

list.insert(123)
list.insert(1222)

list.PrintAll()