# Problem: Linked List Cycle - https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = set()
        curr = head

        while curr:
            if curr in nodes:
                return True
            nodes.add(curr)
            curr = curr.next
        
        return False