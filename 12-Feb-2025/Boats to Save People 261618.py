# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ans = 0
        left = 0
        right = len(people) - 1

        while left <= right:
            # If the weight of the right person is maximal
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            ans += 1
            
        return ans