# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class DoublyNode:
    def __init__(self, val = 0, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Build a doubly linked list
        dummy = DoublyNode()
        pointer = dummy
        curr = head
        while curr:
            node = DoublyNode(curr.val)
            pointer.next = node
            node.prev = pointer
            pointer = node
            curr = curr.next

        first = dummy.next
        last = pointer
        ans = 0

        while first:
            ans = max(ans, first.val + last.val)
            first = first.next
            last = last.prev
        
        return ans