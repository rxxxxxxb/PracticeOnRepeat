class Node:
    def __init__(self,data,string,next):
        self.data = data
        self.string = string

        self.next = next

    def str(self):
        return self.data,self.string



class LinkedList:
    def __init__(self,head = None):
        self.head = head

    def insert(self,data,string):
        node = Node(data,string,self.head)
        d = node.str()
        print(d)

        self.head = node

ll = LinkedList()

ll.insert(100,"One H")
ll.insert(200,"Two H")
ll.insert(300,"Three H")
                