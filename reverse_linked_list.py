class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        curr = head
        prevNode = None
        while curr:
            data = curr.val
            newNode = ListNode(data)
            newNode.next = prevNode
            prevNode = newNode
        return prevNode