from collections import Counter
import math
class Solution:
    def balancedString(self, s: str) -> int:
        total_count = Counter(s)
        window_count = Counter()
        l = r = 0
        n = len(s)
        min_replaced = math.inf
        if self.substringBalanced(total_count, window_count, s):
            return 0
        
        while l < n or r < n:
            window_count[s[r]] += 1
            
            if r == n - 1 and l < n:
                if self.substringBalanced(total_count, window_count, s):
                    min_replaced = min(min_replaced, r - l + 1)
                window_count[s[l]] -= 1
                window_count[s[r]] -= 1
                l += 1       
            elif self.substringBalanced(total_count, window_count, s):
                min_replaced = min(min_replaced, r - l + 1)
                window_count[s[l]] -= 1
                window_count[s[r]] -= 1
                l += 1
            else:
                r += 1
        
        return min_replaced
        

    def substringBalanced(self, total_count, window_count, s):
            string = 'QWER'
            k = len(s) // 4

            for letter in string:
                if total_count[letter] - window_count[letter] > k:
                    return False
            return True

c = Counter('AAABFBDFBDASA')
print(c.most_common()[0][0])
        