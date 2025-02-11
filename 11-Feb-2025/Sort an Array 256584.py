# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        sorted_nums = self.mergeSort(nums)
        return sorted_nums

    def mergeSort(self, nums):
        if len(nums) > 1:
            mid = (0 + len(nums)) // 2
            left_half = nums[:mid]
            right_half = nums[mid:]
            left = self.mergeSort(left_half)
            right = self.mergeSort(right_half)
            return self.merge(left, right)
        else:
            return nums

    def merge(self, nums1, nums2):
        temp = []
        i = j = k = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                temp.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                temp.append(nums2[j])
                j += 1
        
        temp.extend(nums1[i:] + nums2[j:])
        return temp