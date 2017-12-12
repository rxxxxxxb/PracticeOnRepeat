class LinkedStack:

    #-------------------------- nested Node class --------------------------
    class Node:
        slots = 'element', 'next'  # streamline memory usage
        
        def __init__(self, element, next):
            # initialize node’s fields
            self.element = element  # reference to user’s element
            self.next = next  # reference to next node

    def __init__(self):
#”””Create an empty stack.”””
        self.head = None  # reference to the head node
        self.size = 0  # number of stack elements

    def len(self):
#Return the number of elements in the stack.”””
        return self.size

    def isempty(self):
#Return True if the stack is empty.”””
        return self.size == 0

    def push(self, e):
#Add element e to the top of the stack.”””
        self.head = self.Node(e, self.head)  # create and link a new node
        self.size += 1

    def top(self):#Return(but do not remove) the element at the top of the stack.
        if self.isempty():
            raise Exception('Stack is empty')
        return self.head.element  # top of stack is at head of list

    def pop(self):
    #Remove and return the element from the top of the stack(i.e., LIFO)
     #Raise Empty exception if the stack is empty.
        if self.isempty():
            raise Exception('Stack is empty')
        answer = self.head.element
        self.head = self.head.next  # bypass the former top node
        self.size =- 1
        return answer



link = LinkedStack()

for val in range(5):
    
    val = val + 1 
    print(val)
    link.push(val)

top = link.top()
pop = link.pop()
checkEmpty  = link.isempty()
popAgain = link.pop()

print(top,pop)
print(link.top())
print(checkEmpty)
print(popAgain)