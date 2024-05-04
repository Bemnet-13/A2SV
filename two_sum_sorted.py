class Solution:
    def twoSum(self, numbers, target):
        # Initialize a pointer l to be 0

        l = 0
        r = len(numbers) - 1
        not_found = True
        while not_found:
            two_sum = numbers[l] + numbers[r]
            if two_sum == target:
                not_found = False
            elif two_sum > target:
                r -= 1
            else:
                l += 1
        return [l + 1, r + 1]
        