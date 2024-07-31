# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        return self.listReversal(head, None)
    def listReversal(self, head, prev):
        if head == None:
            return prev
        first = head
        second = head.next
        
        # Swapping pointers
        first.next = prev
        return self.listReversal(second, first)