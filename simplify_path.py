class Solution:
    def simplifyPath(self, path: str) -> str:
        broken_path = path.split('/')
        
        stack = []
        
        for i in broken_path:
            if i == '' or i == '.':
                continue
            elif i == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(i)

        path = '/'.join(stack)
        return '/' + path

    

trial = Solution()
o = trial.simplifyPath(path = "/home/")
print(o)
