class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next

class List:
    def __init__(self,head = None):
        self.head = head


    def input(self,data):
        node = Node(data,self.head)
        self.head = node


    def PrintAll(self):
        current = self.head
        
        while current is not None:
            print(current.data)
            current = current.next


ll = List()

ll.input(40)
ll.input(400)
ll.input(4000)

ll.PrintAll()