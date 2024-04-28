# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
    
        def dfs(i, j):
            if i not in range(n) or j not in range(m) or board[i][j] != 'O':
                return
            
            board[i][j] = 'W'
            
            for x, y in directions:
                up, down = x + i, y + j
                dfs(up, down)
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for i in range(n):
            for j in range(m):
                if i == 0 or i == n -1 or j == 0 or j == m - 1:
                    if board[i][j] == 'O':
                        dfs(i, j)
        
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                
                if board[i][j] == 'W':
                    board[i][j] = 'O'
    
        return board