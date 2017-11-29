class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    class Node:
        def __init__(self,element,next):
            self.element = element
            self.next = next

    def push(self,e):
        self.head = self.Node(e,self.head)
        self.size += 1

    def top(self):
        return self.head.element

    def pop(self):
        pop = self.head.element
        self.head = self.head.next
        return pop

link = LinkedList()

link.push(1000)
link.push(500)
top = link.top()
print(top)

link.pop()
top = link.top()
print(top)
