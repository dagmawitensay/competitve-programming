class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0
        while target != 1:
            if maxDoubles == 0:
                moves += (target -1)
                target = 1
            elif maxDoubles > 0 and target % 2 == 0:
                maxDoubles -= 1
                target //= 2
                moves += 1
            else:
                target -= 1
                moves += 1
        
        return moves