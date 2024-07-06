# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        for src, dest in dislikes:
            graph[src - 1].append(dest - 1)
            graph[dest- 1].append(src - 1)
                
        colors = [0] * n
        def dfs(node, color):
            if colors[node] != 0:
                return colors[node] == color
            
            colors[node] = color
            for neighbor in graph[node]:
                if not dfs(neighbor, -color):
                    return False
        
            return True
        
        for i in range(n):
            if colors[i] == 0:
                if not dfs(i, 1):
                    return False
                
        return True