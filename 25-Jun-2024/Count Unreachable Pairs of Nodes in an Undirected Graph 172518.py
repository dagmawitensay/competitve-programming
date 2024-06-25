# Problem: Count Unreachable Pairs of Nodes in an Undirected Graph - https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        self.parents = {i: i for i in range(n)}
        self.rank = [0] * n

        for a, b in edges:
            self.union(a, b)
        
        groups = defaultdict(int)

        for key, val in self.parents.items():
            groups[self.find(val)] += 1
        
        total = 0
        square_total = 0
        for key, val in groups.items():
            total += val
            square_total += val ** 2
        
        return int(0.5 * (total ** 2 - square_total))

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
