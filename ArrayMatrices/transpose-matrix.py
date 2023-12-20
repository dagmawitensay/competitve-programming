class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])
        new_matrix = [[0 for i in range(n)] for j in range(m)]
        
        for i in range(m):
            for j in range(n):
                new_matrix[i][j] = matrix[j][i]
        
        return new_matrix