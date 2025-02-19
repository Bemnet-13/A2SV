# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        curr = self.head
        i = 0
        while i < index:
            i += 1
            curr = curr.next
        
        return curr.val
        
    def addAtHead(self, val: int) -> None:

        new_head = Node(val)
        new_head.next = self.head
        if self.tail is None or self.head is None:
            self.tail = new_head
        self.head = new_head
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_tail = Node(val)
        self.size += 1
        
        if self.tail is None:
            self.head = new_tail
            self.tail = new_tail
            return
        
        self.tail.next = new_tail
        self.tail = new_tail

    
    def printer(self):
        curr = self.head
        while curr:
            print(curr.val, end = " => ")
            curr = curr.next

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        
        if index == 0:
            self.addAtHead(val)
            return
        
        if index == self.size:
            self.addAtTail(val)
            return
        
        curr = self.head
        i = 0

        while i < index - 1:
            i += 1
            curr = curr.next
        
        new_node = Node(val)
        new_node.next = curr.next
        curr.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        
        dummy = Node()
        dummy.next = self.head
        curr = dummy
        i = 0
        while i < index and curr.next:
            i += 1
            curr = curr.next
        
        self.printer()
        curr.next = curr.next.next
        if curr.next == None:
            self.tail = curr
        self.head = dummy.next

        self.size -= 1




# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)