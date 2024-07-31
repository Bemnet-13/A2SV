# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        
        curr = dummy.next
        
        while curr and curr.next:
            curr.val , curr.next.val = curr.next.val, curr.val
            curr = curr.next.next
        
        return dummy.next