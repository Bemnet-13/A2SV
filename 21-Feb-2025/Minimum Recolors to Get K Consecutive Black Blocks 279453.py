# Problem: Minimum Recolors to Get K Consecutive Black Blocks - https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        s = blocks
        counter = Counter(s[:k - 1])
        min_recolors = k

        for end in range(k - 1, len(blocks)):
            counter[s[end]] += 1
            min_recolors = min(min_recolors, counter['W'])
            counter[s[end - k + 1]] -= 1
        
        return min_recolors
