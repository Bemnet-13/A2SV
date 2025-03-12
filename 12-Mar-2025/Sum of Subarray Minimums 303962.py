# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        forward = [1] * len(arr)

        for i in range(len(arr)):
            while stack and arr[stack[-1]] >= arr[i]:
                index = stack.pop()
                forward[index] = i - index
            
            stack.append(i)
        
        i = len(arr)
        while stack:
                index = stack.pop()
                forward[index] = i - index
        
        backward = [1] * len(arr)
        
        for i in range(len(arr) - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                index = stack.pop()
                backward[index] = index - i
            
            stack.append(i)
        
        i = -1
        while stack:
                index = stack.pop()
                backward[index] = index - i

        ans = 0
        for i in range(len(arr)):
            ans += arr[i] * forward[i] * backward[i]
        return ans % (10**9 + 7)