# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        head = None
        nextHead = None
        if list1 and list2:
            if list1.val > list2.val:
                head = list2
                nextHead = list1
            else:
                head = list1
                nextHead = list2
        elif not list1 or not list2:
            return list1 if list1 else list2

        curr = head.next
        prevNode = head

        while curr or nextHead:
            if curr and not nextHead:
                newNode = ListNode(curr.val)
                curr = curr.next
            elif nextHead and not curr:
                newNode = ListNode(nextHead.val)
                nextHead = nextHead.next
            elif curr.val < nextHead.val:
                newNode = ListNode(curr.val)
                curr = curr.next
            elif curr.val >= nextHead.val:
                newNode = ListNode(nextHead.val)
                nextHead = nextHead.next
            prevNode.next = newNode
            prevNode = newNode
        return head
            
