# Problem: Shortest Bridge - https://leetcode.com/problems/shortest-bridge/

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        n = len(grid)

        def isValid(row, col):
            return 0 <= row < n and 0 <= col < n

        start_x, start_y = 0, 0

        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    start_x, start_y = i, j
                    break
        
        queue = deque([(start_x, start_y)])
        second_queue = deque([(start_x, start_y)])
        grid[start_x][start_y] = 2

        while queue:
            row, col = queue.popleft()
            for x, y in directions:
                row_change, col_change = x + row, y + col
                if isValid(row_change, col_change) and grid[row_change][col_change] == 1:
                    queue.append((row_change, col_change))
                    second_queue.append((row_change, col_change))
                    grid[row_change][col_change] = 2
            
        min_distance = 0

        while second_queue:
            new_queue = []
            for row, col in second_queue:
                for x, y in directions:
                    row_change, col_change = x + row, y + col
                    if isValid(row_change, col_change):
                        if grid[row_change][col_change] == 1:
                            return min_distance
                        elif grid[row_change][col_change] == 0:
                            new_queue.append((row_change, col_change))
                            grid[row_change][col_change] = -1
            
            second_queue = new_queue
            min_distance += 1