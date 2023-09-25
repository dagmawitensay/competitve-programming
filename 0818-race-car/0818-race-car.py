from collections import deque
class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1, 0)])
        visited = set()
        
        while queue:
            node, speed, dist = queue.popleft()
            if node == target:
                return dist

            visited.add((node, speed))
            if (node + speed, speed * 2) not in visited:
                queue.append((node + speed, speed * 2, dist + 1))
            if (node + speed > target and speed > 0) or (node + speed < target and speed < 0):
                if speed > 0:
                    iter_speed = -1
                else:
                    iter_speed = 1
                if (node, iter_speed) not in visited:
                    queue.append((node, iter_speed, dist + 1))

        return -1