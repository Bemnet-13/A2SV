# Problem: Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter, seen = Counter(), set()
        start = end = max_length = 0

        while end < len(s):
            if end not in seen:
                counter[s[end]] += 1
                seen.add(end)

            current_length = end - start + 1
            
            if current_length - counter.most_common()[0][1] > k:
                counter[s[start]] -= 1
                start += 1
                max_length = max(max_length, end - start + 1)

            else:
                end += 1
        max_length = max(max_length, end - start)
        return max_length