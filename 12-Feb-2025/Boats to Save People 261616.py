# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ans = 0
        left = 0
        right = len(people) - 1

        while left <= right:
            # If the weight of the right person is maximal
            if people[right] == limit or people[left] + people[right] > limit:
                ans += 1
                right -= 1
            else:
                ans += 1
                left += 1
                right -= 1

        
        return ans