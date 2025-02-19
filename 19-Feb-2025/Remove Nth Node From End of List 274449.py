# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
        
        index = 0
        dummy = ListNode(0, head)
        curr = dummy
        while curr and index < size - n:
            index += 1
            curr = curr.next
        
        curr.next = curr.next.next
        return dummy.next