# Problem: Contiguous Array - https://leetcode.com/problems/contiguous-array/

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashMap = { 0 : -1}
        max_length = 0
        count = 0

        for i in range(len(nums)):
            count += pow(-1, nums[i] + 1)
            print(count)

            if count in hashMap:
                max_length = max(max_length, i - hashMap[count])
            else:
                hashMap[count] = i
        
        return max_length