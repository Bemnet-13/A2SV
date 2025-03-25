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
                    if not path or (dir_ == 'D' and i < int(path[-1])) or dir_ == 'I':
                        if path:
                            new_index = index + 1
                        else:
                            new_index = index
                        path.append(str(i))
                        seen.add(i)
                        backtrack(path, new_index, seen)
                        path.pop()
                        seen.remove(i)

        backtrack([], 0, set())
        return ans