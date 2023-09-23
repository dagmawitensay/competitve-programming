from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque([('0000', 0)])
        visited = set(deadends)
        if '0000' in visited:
            return -1
        
        while queue:
            state, level = queue.popleft()
            if state == target:
                return level
            
            for i in range(4):
                for move in (-1, 1):
                    next_state = state[:i] + str((int(state[i]) + move) % 10) + state[i+1:]
                    if next_state not in visited:
                        visited.add(next_state)
                        queue.append((next_state, level + 1))
        
        return -1