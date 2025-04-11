# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)

        head = n + 1
        for i in range(len(manager)):
            if i == headID:
                continue
            direct_manager = manager[i]
            time = informTime[direct_manager]
            graph[direct_manager].append((i, time))
        
        def dfs(curr_employee):
            if graph[curr_employee] == []:
                return 0
            
            max_time = 0
            for subordinate in graph[curr_employee]:
                time = subordinate[1]
                max_time = max(max_time, dfs(subordinate[0]))
            
            return time + max_time
        
        return dfs(headID)