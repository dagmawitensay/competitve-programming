# Problem: Count Sub Islands - https://leetcode.com/problems/count-sub-islands/

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def isValid(i, j):
            return 0 <= i < m and 0 <= j < n

        def dfs(i, j):
            grid2[i][j] = 2

            for x, y in directions:
                up, down = x + i, y + j
                if isValid(up, down) and grid2[up][down] == 1 and grid1[up][down] == 1:
                    dfs(up, down)
        

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and grid1[i][j] == 0:
                    dfs(i, j)
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and grid1[i][j] == 1:
                    dfs(i, j)
                    count += 1
        
        return count

