from collections import Counter
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        most_F = self.confusion(answerKey, "F", "T",k)
        most_T = self.confusion(answerKey, "T", "F",k)
        return max(most_F, most_T)
        
    def confusion(self, answerkey, reqKey, othKey, k):
        c = Counter()
        l = r = max_consecutive = 0

        while r < len(answerkey):
            c[answerkey[r]] += 1
            if c[othKey] <= k:
                max_consecutive = max(max_consecutive, c[reqKey] + c[othKey])
                r += 1
            else:
                while c[othKey] > k:
                    c[answerkey[l]] -= 1
                    l += 1
                c[answerkey[r]] -= 1
        
        return max_consecutive 
