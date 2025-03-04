# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counts = defaultdict(int)
        ans = 0

        for a in answers:
            counts[a] += 1
            if counts[a] > a + 1:
                ans += a + 1
                counts[a] = 1
        
        ans += sum(counts.keys()) + len(counts.keys())
        return ans