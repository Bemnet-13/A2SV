# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head):
        # Edge cases
        # If there are no elements
        if head == None:
            return None
        elif head.next == None:
            return head
        elif head.next.next == None:
            return head
        
        odd = head
        even = head.next
        
        
        prevOdd = ListNode(odd.val)
        prevEven = ListNode(even.val)
        newOddHead = prevOdd
        newEvenHead = prevEven

        odd = odd.next.next
        even = even.next.next

        while odd or even:
            if odd:
                newOdd = ListNode(odd.val)
                prevOdd.next = newOdd
            if even:
                newEven = ListNode(even.val)
                prevEven.next = newEven
            prevEven , prevOdd = newEven, newOdd
            if odd.next and even.next:
                odd = odd.next.next
                even = even.next.next
            else:
                break
        curr = newOddHead
        while curr.next:
            curr = curr.next
        curr.next = newEvenHead
        return newOddHead