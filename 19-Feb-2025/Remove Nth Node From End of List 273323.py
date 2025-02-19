# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
        
        index = 0

        dummy = ListNode(0, head)
        prev = dummy
        curr = prev.next
        while curr and index < size - n:
            index += 1
            prev = curr
            curr = curr.next
        
        prev.next = curr.next
        return dummy.next
