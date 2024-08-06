# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head):
        self.swap(head)
        return head   
    def swap(self, head):
        if head == None:
            return
        head.val, head.next.val = head.next.val, head.val
        self.swap(head.next.next)

one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)

one.next = two
two.next = three
three.next = four

trial = Solution()
o = trial.swapPairs(one)
print(o.val, o.next.val, o.next.next.val, o.next.next.next.val)