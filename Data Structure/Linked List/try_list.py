class Node:
    def __init__(self,data,next):
        self.next = next
        self.data = data
    
    def data(self): 
        return self.data   

head = 0
head = Node(5,head)
print("h1",head.data)

h2 = Node(20,head)
print("h2", h2.data)

h3 = Node(200, h2)
print("h3", h2.data)

h4 = Node(2000, h2)
print("h4", head.data)

print(head.data)
print(h2.data)
print(h3.data)
print(h4.data)
