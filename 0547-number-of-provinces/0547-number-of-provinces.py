class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j]:
                    graph[i].append(j)
        visited = set()
        
        def dfs(graph, visited, node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(graph, visited, neighbor)
        
        count = 0
        for i in range(len(isConnected)):
            if i not in visited:
                count += 1
                dfs(graph, visited, i)
                
        return count
    