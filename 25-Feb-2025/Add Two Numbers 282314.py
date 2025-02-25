# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nums_1 = 0
        nums_2 = 0
        curr1, curr2 = l1, l2
        curr_mul = 1

        while curr1:
            nums_1 = nums_1 + curr_mul * curr1.val
            curr_mul *= 10
            curr1 = curr1.next
        curr_mul = 1
        while curr2:
            nums_2 = nums_2 + curr_mul * curr2.val
            curr_mul *= 10
            curr2 = curr2.next
        
        ans = nums_1 + nums_2       
        dummy = ListNode()
        curr = dummy
        if ans == 0:
            return ListNode(0)

        while ans:
            ans, mod = divmod(ans, 10)
            new_node = ListNode(mod)
            curr.next = new_node
            curr = new_node
        return dummy.next

