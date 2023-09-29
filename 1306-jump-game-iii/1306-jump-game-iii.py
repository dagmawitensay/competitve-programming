from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque([(start, arr[start])])
        visited = set((start, arr[start]))
        
        while queue:
            x, y = queue.popleft()
            if y == 0:
                return True
            
            add = x + y
            sub = x - y
            if (add < len(arr)) and (add, arr[add]) not in visited:
                queue.append((add, arr[add]))
                visited.add((add, arr[add]))
            if (sub >= 0) and (sub, arr[sub]) not in visited:
                queue.append((sub, arr[sub]))
                visited.add((sub, arr[sub]))
        
        return False
        