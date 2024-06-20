# Problem: Longest Cycle in a Graph - https://leetcode.com/problems/longest-cycle-in-a-graph/

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        indegree = [0] * len(edges)
        visited = [False] * len(edges)
        queue = deque()

        for edge in edges:
            if edge != -1:
                indegree[edge] += 1
            
        
        for i, val in enumerate(indegree):
            if val == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            visited[node] = True
            nbr = edges[node]
            if nbr != -1:
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    queue.append(nbr)
        
        res = -1

        for i in range(len(edges)):
            if not visited[i]:
                nbr = edges[i]
                count = 1
                visited[i] = True

                while nbr != -1 and not visited[nbr]:
                    visited[nbr] = True
                    count += 1
                    nbr = edges[nbr]
                
                res = max(res, count)
        
        
        return res
        

