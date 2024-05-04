#User function Template for python3

class Solution:
    def arraySortedOrNot(self, arr, n):
        r = 1
        while r < len(arr):
            if arr[r - 1] > arr[r]:
                return False
            r += 1
        return True