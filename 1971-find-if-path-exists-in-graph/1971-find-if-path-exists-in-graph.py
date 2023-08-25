class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)
        
        for src, dest in edges:
            adj[src].append(dest)
            adj[dest].append(src)
        
        def dfs(node, visited=set()):
            visited.add(node)
            if node == destination:
                return True
            
            for neigh in adj[node]:
                if neigh not in visited:
                    if dfs(neigh):
                        return True
            
            return False
    
        if dfs(source):
            return True
        
        return False