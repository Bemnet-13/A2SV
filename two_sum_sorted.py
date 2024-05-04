class Solution:
    def twoSum(self, numbers, target):
        # Initialize a pointer l to be 0

        l = 0

        while l < len(numbers):
            num1 = numbers[l]
            num2 = target - num1
            r = l + 1
            while r < len(numbers):
                if numbers[r] == num2:
                    return [l + 1, r + 1]
                elif numbers[r] > num2:
                    break
            l += 1
        