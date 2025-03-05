# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split('/')
        print(dirs)

        stack = []
        for dir_ in dirs:
            if dir_ != "" and dir_ != ".." and dir_ != ".":
                stack.append(dir_)
            elif dir_ == "..":
                if stack:
                    stack.pop()
        
        return "/" + "/".join(stack)