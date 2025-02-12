# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        chem = 0
        n = len(skill)
        prev = skill[0] + skill[-1]
        for i in range(n // 2):
            left, right = skill[i], skill[n - 1 - i]
            if left + right != prev:
                return -1
            prev = left + right
            chem += left * right
        return chem