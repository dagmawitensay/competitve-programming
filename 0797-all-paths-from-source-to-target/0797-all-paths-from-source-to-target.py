class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        ans = []
        
        def dfs(node, curr=[]):
            curr.append(node)
            if node == n - 1:
                ans.append(curr[:])
                return
            
            for neigh in graph[node]:
                dfs(neigh, curr)
                curr.pop()
                    
        
        dfs(0)
        
        return ans