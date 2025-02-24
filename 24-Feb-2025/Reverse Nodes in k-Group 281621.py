# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        groups = []
        curr = head

        gr = []
        while curr:
            if len(gr) < k:
                gr.append(curr.val)
            else:
                groups.extend(gr[::-1])
                gr = []
                gr.append(curr.val)
            curr = curr.next
        
        if len(gr) == k:
            groups.extend(gr[::-1])
        else:
            groups.extend(gr)
        
        dummy = ListNode()
        working = dummy 
        for node in groups:
            new_node = ListNode(node)
            working.next = new_node
            working = new_node
        
        return dummy.next