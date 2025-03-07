# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class NodeItem:
    def __init__(self, val = 0, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class MyCircularDeque:
    def __init__(self, k: int):
        self.limit = k
        self.size = 0
        self.front, self.back = NodeItem(), NodeItem()
        self.front.next = self.back
        self.back.prev = self.front

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        
        newfront = NodeItem(value)
        mid = self.front.next
        self.front.next = newfront
        newfront.next = mid
        mid.prev = newfront
        newfront.prev = self.front
        self.size += 1
        return True 

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        
        newback = NodeItem(value)
        mid = self.back.prev
        self.back.prev = newback
        newback.next = self.back
        mid.next = newback
        newback.prev = mid
        self.size += 1
        return True 

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        self.front.next = self.front.next.next
        self.front.next.prev = self.front
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.back.prev = self.back.prev.prev
        self.back.prev.next = self.back
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return - 1
        return self.front.next.val

    def getRear(self) -> int:
        if self.isEmpty():
            return - 1
        return self.back.prev.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.limit


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()