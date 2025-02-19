# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev = None
        curr = head
        while curr:
            new_node = ListNode(curr.val)
            new_node.next = prev
            prev = new_node
            curr = curr.next
        
        curr = head
        while curr:
            if curr.val != prev.val:
                return False
            curr = curr.next
            prev = prev.next
        
        return True