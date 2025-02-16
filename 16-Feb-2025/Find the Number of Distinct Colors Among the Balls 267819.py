# Problem: Find the Number of Distinct Colors Among the Balls - https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ans = []
        color_count = defaultdict(int)
        ball_to_color = {}

        for x, y in queries:
            color_count[y] += 1
            prev_color = ball_to_color.get(x, -1)
            if prev_color == y:
                color_count[y] -= 1
            elif prev_color != -1:
                color_count[prev_color] -= 1
                if color_count[prev_color] == 0:
                    del color_count[prev_color]
            
            ball_to_color[x] = y
            ans.append(len(color_count))
        
        return ans