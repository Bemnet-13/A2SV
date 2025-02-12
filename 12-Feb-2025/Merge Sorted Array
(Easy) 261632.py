# Problem: Merge Sorted Array
(Easy) - https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = right = 0
        left_swaps = 0
        curr_empty = m
        
        while left < n + m and right < n:
            # If one of them are out of bound
            if left_swaps >= m:
                nums1[left] = nums2[right]
                left += 1
                right += 1
            # If both of them are inbound
            elif nums1[left] <= nums2[right]:
                left += 1
                left_swaps += 1
            else:
                # Free up the space and shift the elements by one place
                k = curr_empty
                while k > left:
                    nums1[k - 1], nums1[k] = nums1[k], nums1[k -1]
                    k -= 1
                nums1[left] = nums2[right]
                left += 1
                right += 1
                curr_empty += 1