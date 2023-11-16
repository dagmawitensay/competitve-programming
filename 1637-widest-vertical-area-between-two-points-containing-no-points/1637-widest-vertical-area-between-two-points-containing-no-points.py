class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        widest = 0
        
        for i in range(1, len(points)):
            widest = max(widest, points[i][0] - points[i - 1][0])
        
        return widest
        