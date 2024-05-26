# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        self.parents = {i: i for i in range(n)}
        self.rank = [0] * n
        self.minScore = defaultdict(lambda: float('inf'))
        score = float('inf')

        for road in roads:
            a, b, dist = road
            self.union(a - 1, b - 1, dist)
            self.minScore[a - 1] = min(self.minScore[a - 1], dist)
            self.minScore[b - 1] = min(self.minScore[b - 1], dist)
        
        score = float('inf')
        parent = self.find(0)
        for i in range(n):
            if self.find(i) == parent:
                score = min(score, self.minScore[i])
       
        return score
    
    def find(self, point):
        if self.parents[point] == point:
            return point
        
        self.parents[point] = self.find(self.parents[point])
        return self.parents[point]

    def union(self, x, y, dist):
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