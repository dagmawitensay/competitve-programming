class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 0),(0, 1),(1, 0), (0, -1), (-1, 0)]
        m, n = len(board), len(board[0])
        count = Counter(word)
        if count[word[-1]] < count[word[0]]:
            word = word[::-1]
        
        def isValid(i, j):
            return 0 <= i < m and 0 <= j < n
        
        currWord = []
       
        def backtrack(row, col, visited):
            if len(currWord) > len(word):
                return

            if len(currWord) == len(word):
                if "".join(currWord) == word:
                    return True
        
            
            for x, y in directions:
                new_x, new_y = row + x, col + y
                if isValid(new_x, new_y) and (new_x, new_y) not in visited  and word[len(currWord)] == board[new_x][new_y]:
                    visited.add((new_x, new_y))
                    currWord.append(board[new_x][new_y])
                    if backtrack(new_x, new_y, visited):
                        return True
                    visited.remove((new_x, new_y))
                    currWord.pop()
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if backtrack(i, j, set()):
                        return True

        return False