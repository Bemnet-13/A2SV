# Problem: Reverse Pairs - https://leetcode.com/problems/reverse-pairs/description/

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ans = 0
        def mergeSort(left, right):
            if left == right:
                return [nums[left]]
            mid = (left + right) // 2
            left_half = mergeSort(left, mid)
            right_half = mergeSort(mid + 1, right)
            return merge(left_half, right_half)
        
        def merge(left_half, right_half):
            countReversePairs(left_half, right_half)
            merged = []

            i = j = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
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
        
        def countReversePairs(left_half, right_half):
            nonlocal ans
            j = 0
            for i in range(len(left_half)):
                while j < len(right_half) and left_half[i] > 2 * right_half[j]:
                    j += 1
                
                ans += j
        
        mergeSort(0, len(nums) - 1)
        return ans
        