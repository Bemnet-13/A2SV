# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        seen = set()
        dummy = ListNode(0, head)
        prev = dummy
        curr = prev.next

        while curr:
            if curr.val not in seen:
                seen.add(curr.val)
                prev = curr
            else:
                prev.next = curr.next
            
            curr = curr.next
        
        return dummy.next