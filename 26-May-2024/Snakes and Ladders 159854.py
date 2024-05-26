# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board):
        n = len(board)
        board.reverse()

        def Position(block):
            row = (block-1) // n
            col = (block-1) % n
            if row % 2 != 0:
                col = n - 1 - col
            return [row, col]

        q = deque()
        q.append([1,0])
        visited = set()
        while q:
            currBlock, currMoves = q.popleft()
            for i in range(1,7):
                nextBlock = currBlock + i
                row,col = Position(nextBlock)
                if board[row][col] != -1:
                    nextBlock = board[row][col]
                if nextBlock == n*n:
                    return currMoves + 1
                if nextBlock not in visited:
                    visited.add(nextBlock)
                    q.append([nextBlock,currMoves + 1])
        return -1