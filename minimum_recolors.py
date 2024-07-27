class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        color_count = Counter(blocks[:k - 1])
        min_recolor = len(blocks) + 1
        
        for i in range(k - 1, len(blocks)):
            color_count[blocks[i]] += 1
            min_recolor = min(min_recolor, color_count['W'])
            color_count[blocks[i - k + 1]] -= 1
        
        return min_recolor