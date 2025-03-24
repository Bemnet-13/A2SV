# Problem: Find the Punishment Number of an Integer - https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/

class Solution:
    def punishmentNumber(self, n: int) -> int:    
        ans = [False] * n
        def backtrack(path, index, elem, num):
            nonlocal ans
            if index == len(elem):
                if path[-1] == i:
                    ans[num - 1] = True
                return
            
            curr = 0
            for k in range(index, len(elem)):
                curr = curr * 10 + int(elem[k])
                if not path or path[-1] + curr <= n:
                    new_sum = curr
                    if path:
                        new_sum += path[-1]
                    path.append(new_sum)
                    backtrack(path, k + 1, elem, num)
                    path.pop()
                    
        res = 0
        for i in range(1, n + 1):
            backtrack([], 0, str(i ** 2), i)
            if ans[i - 1]:
                res += i ** 2
        
        return res