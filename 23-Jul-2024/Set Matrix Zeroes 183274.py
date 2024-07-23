# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m, n = len(matrix), len(matrix[0])
        visited = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0 and (i, j) not in visited:
                    for col in range(n):
                        if matrix[i][col] != 0:
                            visited.add((i, col))
                        matrix[i][col] = 0
                        
                    
                    for row in range(m):
                        if matrix[row][j] != 0:
                            visited.add((row, j))
                        matrix[row][j] = 0
