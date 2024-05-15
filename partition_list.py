class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head, x: int):
        temp = head
        while temp:
            if temp.val < x:
                break
            temp = temp.next
        # Set the newNode for the partitioned list

        newHead = ListNode(temp.val)
        prevNode = newHead

        while temp:
            if temp.val < x:
                newNode = ListNode(temp.val)
                prevNode.next = newNode
                prevNode = newNode
            temp = temp.next
        
        curr = head
        while curr:
            if curr.val >= x:
                newNode = ListNode(curr.val)
                prevNode.next = newNode
                prevNode = newNode
        return newHead





        