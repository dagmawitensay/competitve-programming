# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.parents = {i: i for i in range(len(edges))}
        self.rank = [0 for i in range(len(edges))]
        x, y = -1, -1

        for s, d in edges:
            if self.isConnected(s - 1, d -1):
                x, y = s, d
            else:
                self.union(s - 1, d - 1)
        
        return [x, y]
            
    
    def find(self, node):
        if node == self.parents[node]:
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
                self.parents[root1] = root2
                self.rank[root2] += 1
    
    def isConnected(self, node1, node2):
        return self.find(node1) == self.find(node2)

