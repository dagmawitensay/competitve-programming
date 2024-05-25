# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        self.parents = {i: i for i in range(len(stones))}
        self.rank = [0] * len(stones)
        edges = []

        for i in range(len(stones)):
            for j in range(len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    edges.append([i, j])
        
        for s, d in edges:
            self.union(s, d)
        
        count = 0

        for key, val in self.parents.items():
            if key != val:
                count += 1
        
        return count
    

    def find(self, node):
        if self.parents[node] == node:
            return node
        
        self.parents[node] = self.find(self.parents[node])
        return self.parents[node]
    
    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parents[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parents[root1] = root2
            else:
                self.parents[root2] = root1
                self.rank[root1] += 1
