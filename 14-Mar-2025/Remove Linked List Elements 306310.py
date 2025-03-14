# Problem: Remove Linked List Elements - https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = head
        prev = dummy
    
        def remover(prev, curr, val):
            if not curr:
                prev.next = curr
                return
            
            if curr.val != val:
                prev.next = curr
                prev = curr
            remover(prev, curr.next, val)
            

        remover(prev, curr, val)
        return dummy.next
            
