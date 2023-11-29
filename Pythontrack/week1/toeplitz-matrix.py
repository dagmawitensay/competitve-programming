class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        val = matrix[0][0]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                r = i - 1
                c = j - 1
                if r >= 0 and c >= 0 and matrix[i][j] != matrix[r][c]:
                    return False
        
        return True