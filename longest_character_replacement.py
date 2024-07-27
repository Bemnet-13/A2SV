class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1
        
        l = longest = 0
        r = 1
        char_count = Counter(s[0])     
        while r < len(s):
            commonest = char_count.most_common()[0][0]
            if s[r] == commonest:
                char_count[s[r]] += 1
                r += 1
                print(commonest, l , r)
            elif char_count[s[r]] == char_count[commonest] or sum(char_count.values()) - char_count[commonest] < k:
                char_count[s[r]] += 1
                print(commonest,l, r)
                r += 1   
            elif l == r:
                char_count[s[r]] += 1
                r += 1
            else:
                char_count[s[l]] -= 1
                l += 1
            longest = max(longest, sum(char_count.values()))
        
        return longest