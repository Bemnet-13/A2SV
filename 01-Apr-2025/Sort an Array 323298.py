# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(0, len(nums) - 1, nums)
    
    def mergeSort(self, left, right, nums):
        if left == right:
            return [nums[left]]
        
        mid = (left + right) // 2
        left_half = self.mergeSort(left, mid, nums)
        right_half = self.mergeSort(mid + 1, right, nums)
        return self.merge(left_half, right_half)
    
    def merge(self, arr1, arr2):
        ans = []
        i = j = 0

        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                ans.append(arr1[i])
                i += 1
            else:
                ans.append(arr2[j])
                j += 1
        
        while i < len(arr1):
            ans.append(arr1[i])
            i += 1
        
        while j < len(arr2):
            ans.append(arr2[j])
            j += 1
        
        return ans