# Problem: Linked List Cycle II - https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Phase 1
        slow = head
        fast = head
        i = 0

        while fast and fast.next:
            print(i, slow.val, fast.val)
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break

        if fast is None or fast.next is None:
            return None
        
        # print(fast.val, slow.val)


        slow = head
        while fast != slow:
            slow = slow.next
            fast = fast.next

        return fast 