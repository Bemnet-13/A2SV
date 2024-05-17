class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head):
        prev = head
        curr = prev.next
        
        while curr:
            currentNumber = curr.val
            temp = head
            while temp != curr:
                if temp == head and currentNumber < temp.val:
                    newNode = ListNode(currentNumber)
                    newNode.next = head
                    head = newNode
                    break
                elif temp.val < currentNumber and currentNumber < temp.next.val:
                    newNode = ListNode(currentNumber)
                    newNode.next = temp.next
                    temp.next = newNode
                    break
                temp = temp.next
            prev.next = curr.next
            curr = prev.next
        return head
            