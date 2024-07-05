# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSort(self, arr):
        for i in range(len(arr) - 1):
            j = i
            while j >= 0:
                if arr[j + 1] < arr[j]:
                    arr[j], arr[j+1] = arr[j+1],arr[j]
                else:
                    break
                j -= 1        
    def sortList(self, head):
        dummy = ListNode()
        dummy.next = head
        current = dummy.next
        _min = 100001
        _max = -1 * 100001
        while current:
            _min = min(_min, current.val)
            _max = max(_max, current.val)
            current = current.next
        
        _range = _max - _min

        # Fixed number of buckets 
        n = 20
        buckets = [[] for _ in range(n + 1)]
        current = dummy.next

        while current:
            buckets[int(n * (current.val - _min) // _range)].append(current.val)
            current = current.next
        # Iterate through the buckets
        dummyNode = ListNode()

        currentNode = dummyNode
        for bucket in buckets:
            self.insertionSort(bucket)
            for k in bucket:
                newNode = ListNode(k)
                currentNode.next = newNode
                currentNode = newNode
        
        return dummyNode.next