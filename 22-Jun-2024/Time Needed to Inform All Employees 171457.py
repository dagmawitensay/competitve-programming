# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for i, val in enumerate(manager):
            graph[val].append(i)
        

        def dfs(node):
            if graph[node] == []:
                return informTime[node]
            

            values = []
            for childNode in graph[node]:
                values.append(dfs(childNode))
            
            return max(values) + informTime[node]
        
        return dfs(headID)
