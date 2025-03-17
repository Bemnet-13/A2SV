# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = defaultdict(lambda : -1)
        stack = []

        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                curr = stack.pop()
                next_greater[curr] = nums2[i]
            
            stack.append(nums2[i])
        
        return [next_greater[i] for i in nums1]