class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(node, visited):
            if node in visited:
                return
            
            visited.add(node)
            for neigh in rooms[node]:
                if neigh != node:
                    dfs(neigh, visited)
        
            return visited
    
        visited = dfs(0, set())
        if len(visited) == len(rooms):
            return True
        
        return False
        