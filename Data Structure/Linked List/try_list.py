class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self,head = None):
        self.head = head

    def input(self,data):
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

ll = LinkedList()
 
ll.input(55)
ll.input(521)
ll.input(5121)
ll.input(51)
ll.input(100)

ll.PrintAll()
