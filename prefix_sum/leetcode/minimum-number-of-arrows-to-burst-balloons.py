class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        
        points.sort()
        first, second = 0, 1
        prev = points[0][1]
        count = 0

        while second < len(points):
            if (points[first][1] >= points[second][0]) and (prev >= points[second][0]):
                prev = min(prev, points[second][1])
            else:
                count += 1
                prev = points[second][1]
                first = second
            
            second += 1
        
        return count + 1