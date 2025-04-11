# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = {}

        for employee in employees:
            id_ = employee.id
            graph[id_] = employee
        
        ans = 0
        visited = set()
        def dfs(id_):
            nonlocal ans
            ans += graph[id_].importance
            visited.add(id_)

            for neighbor in graph[id_].subordinates:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(id)  
        return ans