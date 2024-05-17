# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head, k: int):
        # Locate the nodes
        # Swap their values

        i = 1
        temp = head
        while temp:
            if i == k:
                firstNode = temp
            i += 1
            temp = temp.next
        j = 0
        temp = head
        while temp:
            if j == k - i:
                lastNode = temp
                break
            j += 1
            temp = temp.next
        firstNode.val, lastNode.val = lastNode.val, firstNode.val
        return head