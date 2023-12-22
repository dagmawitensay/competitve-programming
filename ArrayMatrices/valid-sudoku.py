class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict()
        cols = defaultdict()

        positions = [(0, 0), (0, 1), (0, 2),
        (1, 0),  (1, 1),  (1, 2),
        (2, 0),  (2, 1),  (2, 2)]
         
        
        for i in range(9):
            for j in range(9):
                if i not in rows:
                    rows[i] = set()

                if board[i][j] != '.' and board[i][j] in rows[i]:
                    return False

                rows[i].add(board[i][j])
                
                if j not in cols:
                    cols[j] = set()
                
                if board[i][j] != '.' and board[i][j] in cols[j]:
                    return False

                cols[j].add(board[i][j])
            
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                curr_box = set()
                for x, y in positions:
                    if board[x + i][y + j] != "." and board[x + i][y + j] in curr_box:
                        return False
                    curr_box.add(board[x + i][y + j])

        
        return True













        # rows = {
        #     0 : {5, 3, 7}
        #     1: {6}
        # }

        # cols = {
        #     0: {5, 6}
        #     1: {3}
        #     4: {7}
        # }
        # (0, 0), (0, 1), (0, 2)
        # (1, 0)  (1, 1)  (1, 2)
        # (2, 0)  (2, 1)  (2, 2)