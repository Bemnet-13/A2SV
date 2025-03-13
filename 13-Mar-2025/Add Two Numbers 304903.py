# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        def add(l1, l2, curr, carry):
            if not l1 and not l2:
                return ListNode(carry) if carry > 0 else None

            ans = carry
            ans += l1.val if l1 else 0
            ans += l2.val if l2 else 0

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
            curr = ListNode(ans % 10)
            curr.next = add(l1, l2, curr, ans // 10)
            return curr


        return add(l1, l2, curr, 0)
        