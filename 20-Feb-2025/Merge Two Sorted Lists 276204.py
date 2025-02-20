# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                new_node = ListNode(list1.val)
                curr.next = new_node
                curr = new_node
                list1 = list1.next
            else:
                new_node = ListNode(list2.val)
                curr.next = new_node
                curr = new_node
                list2 = list2.next
        
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        
        return dummy.next