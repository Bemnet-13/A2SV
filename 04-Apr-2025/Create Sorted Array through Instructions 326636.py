# Problem: Create Sorted Array through Instructions - https://leetcode.com/problems/create-sorted-array-through-instructions/

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:    
        ans = [[0, 0] for _ in range(len(instructions))]
        instructions = [(i, num) for i, num in enumerate(instructions)]
        
        def mergeSort(left, right):
            if left == right:
                return [instructions[left]]
            
            mid = (left + right) // 2
            left_half = mergeSort(left, mid)
            right_half = mergeSort(mid + 1, right)

            return merge(left_half, right_half)

        def merge(left_half, right_half):
            count_smaller_greater(left_half, right_half)
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

        def count_smaller_greater(left_half, right_half):
            nonlocal ans
            j = 0
            for i in range(len(right_half)):
                while j < len(left_half) and left_half[j][1] < right_half[i][1]:
                    j += 1
                ans[right_half[i][0]][0] += j
            
            n = len(left_half)
            j = 0
            for i in range(len(right_half)):
                while j < len(left_half) and left_half[j][1] <= right_half[i][1]:
                    j += 1
                ans[right_half[i][0]][1] += n - j
        
        mergeSort(0, len(instructions) - 1)
        final = 0
        for min_, max_ in ans:
            final += min(min_, max_)
        return final % (10**9 + 7)