class Solution:
    def dividePlayers(self, skill) -> int:
        skill.sort()

        l = 0
        r = len(skill) - 1
        chemistry = 0
        skill_level = skill[0] + skill[-1]

        while l < r:
            if skill[l] + skill[r] != skill_level:
                return -1
            chemistry += skill[l] + skill[r]
            l += 1
            r -= 1
        return chemistry