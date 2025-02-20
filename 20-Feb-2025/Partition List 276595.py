# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0, head)
        right_part = dummy
        curr = head
        prev = head

        while curr:
            if curr.val >= x:
                new_node = ListNode(curr.val)
                right_part.next = new_node
                right_part = new_node
            elif prev.val >= x and curr.val < x:
                prev.val, curr.val = curr.val, prev.val
                prev = prev.next
            elif prev.val < x:
                prev = prev.next
            
            curr = curr.next

        curr = dummy.next
        while prev:
            prev.val = curr.val
            prev = prev.next
            curr = curr.next
        
        return head