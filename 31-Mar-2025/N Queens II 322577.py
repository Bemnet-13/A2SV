# Problem: N Queens II - https://leetcode.com/problems/n-queens-ii/

class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0

        def isClear(x, y, dirs, prev):
            while 0 <= x < n and 0 <= y < n:
                x = x + dirs[0]
                y = y + dirs[1]
                if (x, y) in prev:
                    return False
            return True
        
        def backtrack(path, seen, prev):
            nonlocal ans
            if len(path) == n:
                ans += 1
                return
            
            for i in range(n):
                if i not in prev:
                    if isClear(i, len(seen), [-1, -1], seen) and \
                     isClear(i, len(seen), [1, -1], seen):
                        path.append(i)
                        prev.add(i)
                        seen.add((i, len(path) - 1))
                        backtrack(path, seen, prev)
                        path.pop()
                        prev.remove(i)
                        seen.remove((i, len(path)))
                        
        backtrack([], set(), set())
        return ans