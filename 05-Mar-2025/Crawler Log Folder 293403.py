# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        path = "".join(logs).split("/")

        print(path)
        stack = []
        for dirs in path:
            if dirs == "..":
                if stack:
                    stack.pop()
            elif dirs != "." and dirs != "":
                stack.append(dirs)
        
        return len(stack)