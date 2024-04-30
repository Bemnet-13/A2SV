# Initialize a node class
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
# Create a stack class
class Stack:
    def __init__(self) -> None:
        self.head = None
    # push operation
    def push(self, val):
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
    # pop operation
    def pop(self) -> any:
        if self.head == None:
            return None
        top = self.head
        self.head = top.next
        return top.data
    
    def peek(self)-> any:
        if self.head == None:
            return None
        top = self.head
        return top.data
    def isEmpty(self) -> bool:
        if self.head:
            return False
        return True
    def stackList(self):
        stack = []
        if self.head == None:
            return stack
        temp = self.head 
        while temp:
            stack.insert(0, temp.data)
            temp = temp.next
        return stack


path = "/home//foo/"

print(path.split('/'))