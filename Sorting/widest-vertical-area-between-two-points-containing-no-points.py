class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        wildest = 0
        
        for i in range(len(points) - 1):
            wildest = max(wildest, points[i + 1][0] - points[i][0])

        return wildest