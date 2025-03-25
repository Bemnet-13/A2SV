# Problem: Construct Smallest Number From DI String - https://leetcode.com/problems/construct-smallest-number-from-di-string/description/

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        ans = ""

        def backtrack(path, index, seen):
            nonlocal ans
            if index == len(pattern):
                ans =  "".join(path[:])
                return
            
            for i in range(1, 10):
                dir_ = pattern[index]
                if not ans and i not in seen:
                    if (dir_ == 'D' and not path or i < int(path[-1])) or dir_ == 'I':
                        path.append(str(i))
                        seen.add(i)
                        backtrack(path, index + 1, seen)
                        path.pop()
                        seen.remove(i)

        for i in range(1, 10):    
            if not ans:
                backtrack([str(i)], 0, set([i]))

        return ans