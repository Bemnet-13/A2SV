# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums1)

        stack = []
        store = {}
        for num in nums2:
            while stack and stack[-1] < num:
                val = stack.pop()
                store[val] = num
            
            stack.append(num)
        
        for i in range(len(ans)):
            if nums1[i] in store:
                ans[i] = store[nums1[i]]
        
        return ans