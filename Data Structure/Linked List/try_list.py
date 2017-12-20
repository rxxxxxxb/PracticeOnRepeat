class Node:
    def __init__(self,data,next):
        self.next = next
        self.data = data
    
    def data(self): 
        return self.data   

class Linked:
    def __init__(self,head = None):
        self.head = head

    def push(self,data):
        node = Node(data,self.head)
        self.head = node
        print(node)
        print(data)
        


link = Linked()

link.push(10)
