from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        target_count = Counter(t)
        c = Counter()
        substring_range = []
        l = r = 0

        while l < len(s):
            if r == len(s) - 1:
                c[s[r]] += 1
                if self.substringIn(c, target_count):
                    substring_range.append([l, r + 1])
                    c[s[l]] -= 1
                l += 1
                c[s[r]] -= 1

            elif s[l] not in target_count and list(c.keys()) == []:
                l += 1
                r += 1
            elif s[l] not in target_count:
                l += 1
            elif s[r] in target_count:
                c[s[r]] += 1
                if self.substringIn(c, target_count):
                    substring_range.append([l, r + 1])
                    c[s[l]] -= 1
                    c[s[r]] -= 1
                    l += 1
                else:
                    r += 1
            else:
                r += 1
        if substring_range == []:
            return ""
        substring_range.sort(key = lambda r:r[1] - r[0])
        l , r = substring_range[0]
        return s[l:r]
    

    def substringIn(self, window_count, target_count):
        for key in target_count:
            if window_count[key] < target_count[key]:
                return False
        return True


trial = Solution()
o = trial.minWindow(s = "a", t = "b")    
print(o)        