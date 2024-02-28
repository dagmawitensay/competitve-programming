class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rowMax = []
        colMax = []
        for row in grid:
            rowMax.append(max(row))
        
        maxVal = grid[0][0]
        for i in range(len(grid[0])):
            maxVal = float('-inf')
            for j in range(len(grid)):
                maxVal = max(maxVal, grid[j][i])
            colMax.append(maxVal)
        
        total = 0
        for i in range(len(rowMax)):
            for j in range(len(colMax)):
                total += (min(rowMax[i], colMax[j]) - grid[i][j])
    
        return total