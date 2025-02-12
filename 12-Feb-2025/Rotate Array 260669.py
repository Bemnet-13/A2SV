# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Use a set to know which indices are visited
        # If the running index and the fixed index overlap we stop
        # If an index is visited, then move the pointer by one and do the swapping again

        fixed = k
        seen = set()
        running = 0
        temp = nums[0]
        n = len(nums)

        while len(seen) < len(nums):
            # Get the second position in a temp varaible

            # The current index is seen
            seen.add(running)
            curr = temp

            temp = nums[(running + k) % n]
            nums[(running + k) % n] = curr
            running = (running + k) % n
            if running in seen:
                running += 1
                temp = nums[running % n]

            # print(running)
