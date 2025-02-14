# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)
        curr_counter = Counter()
        left = 0
        min_index = len(s)
        max_index = -1

        for right in range(len(s)):
            curr_counter[s[right]] += 1
            while curr_counter >= target:
                if right - left < abs(min_index - max_index):
                    min_index = left
                    max_index = right
                curr_counter[s[left]] -= 1
                left += 1
        
        return s[min_index:max_index + 1]