# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:  
    def sortList(self, head):

        def mergeSort(node):
            if not node or not node.next:
                return node
                
            dummy = ListNode()
            left = dummy
            fast = node
            
            while fast and fast.next:
                left.next = node
                left = left.next
                node = node.next
                fast = fast.next.next
            right = node
            left.next = None
            
            left_half = mergeSort(dummy.next)
            right_half = mergeSort(right)
            return merge(left_half, right_half)

        def merge(left_half, right_half):
            dummy = ListNode()
            curr = dummy
            while left_half and right_half:
                if left_half.val < right_half.val:
                    curr.next = left_half
                    curr = curr.next
                    left_half = left_half.next
                else:
                    curr.next = right_half
                    curr = curr.next
                    right_half = right_half.next
            if left_half:
                curr.next = left_half
            if right_half:
                curr.next = right_half
            
            return dummy.next

        return mergeSort(head)