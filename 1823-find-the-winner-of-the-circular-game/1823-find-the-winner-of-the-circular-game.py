from collections import deque
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = deque(range(1, n + 1))
        count = 1
        while len(queue) != 1:
            if count < k:
                queue.append(queue.popleft())
                count += 1
            else:
                count = 1
                queue.popleft()
        
        return queue[0]