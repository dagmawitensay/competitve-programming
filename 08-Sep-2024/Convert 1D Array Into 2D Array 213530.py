# Problem: Convert 1D Array Into 2D Array - https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        matrix = [[0 for i in range(n)] for j in range(m)]
        rows = len(original) // n
        
        if rows != m or (len(original) // rows) != n:
            return []

        for i in range(len(original)):
            row = i // n
            col = i % n
            matrix[row][col] = original[i]
        
        return matrix