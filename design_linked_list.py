class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        # If the list is empty

        if not self.head:
            return -1
        # If the index is a valid index
        curr = self.head
        k = 0
        while curr:
            if k == index:
                return curr.val
            curr = curr.next
            k += 1
        # If the index is a valud index
        return -1

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        self.size += 1


    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        self.size += 1
        if not self.head:
            self.head = newNode
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        
        curr.next = newNode



    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index > self.size:
            return
        else:
            k = 0
            prev = self.head
            curr = prev.next
            while curr and k < index:
                prev = curr
                curr = curr.next
                k += 1
            newNode= Node(val)
            prev.next = newNode
            newNode.next = curr
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        self.size -= 1
        if not self.head:
            return
        if index == 0:
            self.head = self.head.next
            return
        else:
            k = 0
            prev = self.head
            curr = prev.next
            while curr and k < index - 1:
                prev = curr
                curr = curr.next
                k += 1
            prev.next = curr.next



class Node:
    def __init__(self, val):
        self.val = val
        self.next = next

ll = MyLinkedList()
ll.addAtHead(1)
ll.addAtTail(2)
print(ll.llAsList())