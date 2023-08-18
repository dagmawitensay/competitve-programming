class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegrees = [0] * n
        ans = []
        
        
        for edge in edges:
            indegrees[edge[1]] += 1
        
        for i in range(n):
            if indegrees[i] == 0:
                ans.append(i)
        
        
        return ans