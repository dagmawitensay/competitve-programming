class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        click_x = click[0]
        click_y = click[1]
        
        if board[click_x][click_y] == 'M':
            board[click_x][click_y] = 'X'
            return board
        
        n, m = len(board), len(board[0])
        
        def dfs(i, j):
            if i in [-1, n] or j in [-1, m] or board[i][j] != 'E':
                return
            
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1), (-1, -1), (1, 1)]
            mines = 0
            for x, y in directions:
                up, down = x + i, y + j
                if up in range(n) and down in range(m) and board[up][down] == 'M':
                    mines += 1
            
            if mines:
                board[i][j] = str(mines)
            else:
                board[i][j] = 'B'
                for x, y in directions:
                    up, down = x + i, y + j
                    dfs(up, down)
                   
        dfs(click_x, click_y)
    
        return board
            
            