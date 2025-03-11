# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        minimum = [0] * len(nums)
        stack = []

        for i in range(len(nums)):
            if i == 0:
                pass
            elif nums[i] < nums[minimum[i - 1]]:
                minimum[i] = i
            else:
                minimum[i] = minimum[i - 1]
            
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            
            if stack and nums[minimum[stack[-1]]] < nums[i]:
                return True
            
            stack.append(i)

        return False