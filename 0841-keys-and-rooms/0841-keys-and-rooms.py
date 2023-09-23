from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        visited = set()
        visited.add(0)
        while queue:
            node = queue.popleft()
            for child in rooms[node]:
                if child != node and child not in visited:
                    queue.append(child)
                    visited.add(child)
        print(visited)
        if len(visited) == len(rooms):
            return True
        
        return False