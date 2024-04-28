# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        res = [False] * len(queries)
        self.parents = {i: i for i in range(n)}
        self.rank = [0] * n

        for i in range(len(queries)):
            queries[i].append(i)
        
        queries.sort(key=lambda x: x[2])
        edgeList.sort(key=lambda x: x[2])
        i = 0

        for src, dest, limit, index in queries:
            while i < len(edgeList) and edgeList[i][2] < limit:
                self.union(edgeList[i][0], edgeList[i][1])
                i += 1
            
            if self.isConnected(src, dest):
                res[index] = True
        
        return res


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
