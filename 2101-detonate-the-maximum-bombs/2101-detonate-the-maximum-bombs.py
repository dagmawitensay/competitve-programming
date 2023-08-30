class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        graph2 = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(1, len(bombs)):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                d = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                if d <= r1:
                    graph[i].append(j)
                
                if d <= r2:
                    graph[j].append(i)
        
        
        def dfs(node, visited):
            if node in visited:
                return 0
            
            visited.add(node)
            for neigh in graph[node]:
                dfs(neigh, visited)
            
            return len(visited)
        
        res = 0
        
        for i in range(len(bombs)):
            res = max(res, dfs(i, set()))
        
        return res