# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        self.parents = {i: i for i in range(len(points))}
        self.rank = [0] * len(points)
        cost = 0
        edges = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = (abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]))
                edges.append((dist, i, j))
        
        edges.sort()

        for edge in edges:
            dist, s, d = edge
            if not self.isConnected(s, d):
                cost += dist
                self.union(s, d)
        
        return cost
    
    def find(self, point):
        if self.parents[point] == point:
            return point
        
        self.parents[point] = self.find(self.parents[point])
        return self.parents[point]

    def union(self, x, y):
        root1 = self.find(x)
        root2 = self.find(y)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parents[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parents[root1] = root2
            else:
                self.parents[root1] = root2
                self.rank[root2] += 1 
    
    def isConnected(self, x, y):
        return self.find(x) == self.find(y)