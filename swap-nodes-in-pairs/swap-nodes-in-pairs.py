class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head):
        self.swap(head)
        return head   
    def swap(self, head):
        if head == None or head.next == None:
            return
        head.val, head.next.val = head.next.val, head.val
        self.swap(head.next.next)