# Problem: Count of Smaller Numbers After Self - https://leetcode.com/problems/count-of-smaller-numbers-after-self/

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        nums = [(i, num) for i, num in enumerate(nums)]

        def mergeSort(nums, left, right):
            if left == right:
                return [nums[left]]
            
            mid = (left + right) // 2
            left_half = mergeSort(nums, left, mid)
            right_half = mergeSort(nums, mid + 1, right)
            return merge(left_half, right_half)
        
        def merge(left_half, right_half):
            count_smaller(left_half, right_half)
            merged = []

            i = j = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i][1] < right_half[j][1]:
                    merged.append(left_half[i])
                    i += 1
                else:
                    merged.append(right_half[j])
                    j += 1
            
            while i < len(left_half):
                merged.append(left_half[i])
                i += 1  
            while j < len(right_half):
                merged.append(right_half[j])
                j += 1  

            return merged              
        
        def count_smaller(left_half, right_half):
            nonlocal ans
            j = 0
            for i in range(len(left_half)):
                while j < len(right_half) and left_half[i][1] > right_half[j][1]:
                    j += 1
                ans[left_half[i][0]] += j
        
        mergeSort(nums, 0, len(nums) - 1)
        return ans