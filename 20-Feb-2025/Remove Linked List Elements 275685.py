# Problem: Remove Linked List Elements - https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        curr = prev.next

        while curr:
            if curr.val != val:
                prev.next = curr
                prev = curr

            curr = curr.next
        
        prev.next = curr

        return dummy.next
