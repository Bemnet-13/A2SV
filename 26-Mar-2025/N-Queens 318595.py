# Problem: N-Queens - https://leetcode.com/problems/n-queens/description/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []

        def isClear(x, y, dirs, prev):
            while 0 <= x < n and 0 <= y < n:
                x = x + dirs[0]
                y = y + dirs[1]
                if (x, y) in prev:
                    return False
            return True
        
        def boardCons(path):
            ans = [["."] * n for _ in range(n)]
            k = 0
            for i in path:
                ans[k][i] = 'Q'
                ans[k] = "".join(ans[k])
                k += 1
            return ans
        
        def backtrack(path, seen, prev):
            if len(path) == n:
                ans.append(boardCons(path[:]))
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

