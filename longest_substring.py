class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Use sets
        character_count = set()
        max_length = 0
        l = r = 0
        while r < len(s):
            if s[r] not in character_count:
                character_count.add(s[r])
                max_length = max(max_length, len(character_count))
                r += 1
            else:
                character_count.remove(s[l])
                l += 1
        return max_length