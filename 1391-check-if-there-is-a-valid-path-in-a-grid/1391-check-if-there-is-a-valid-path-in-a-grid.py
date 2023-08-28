class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        directions = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }
        
        n, m = len(grid), len(grid[0])
        
        def isValid(row, col):
            return (0 <= row < n and 0 <= col < m and grid[row][col] != 0)
        
        def dfs(row, col):
            if row == n - 1 and col == m - 1:
                return True
            
            grid[row][col], d = 0, grid[row][col]
            
            for row_change, col_change in directions[d]:
                new_row, new_col = row + row_change, col + col_change
                if isValid(new_row, new_col) and (-row_change, -col_change) in  directions[grid[new_row][new_col]]:
                    if dfs(new_row, new_col):
                        return True
                        
            return False
        
        return dfs(0, 0)