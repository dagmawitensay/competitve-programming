# Problem: Similar String Groups - https://leetcode.com/problems/similar-string-groups/

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        self.parents = {i: i for i in range(n)}
        self.rank = [0] * n
        for i in range(n):
            for j in range(i + 1, n):
                if self.count_difference(strs[i], strs[j]):
                    self.union(i, j)
        
        groups = set()
        for k, v in self.parents.items():
            groups.add(self.find(k))
        
        return len(groups)
    
    def count_difference(self, str1, str2):
        count = 0
        for i in range(min(len(str1), len(str2))):
            if str1[i] != str2[i]:
                count += 1
            
            if count > 2:
                return False
        
        return True
    
    def find(self, node):
        if self.parents[node] == node:
            return node
        
        self.parents[node] = self.find(self.parents[node])
        return self.parents[node]
    
    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parents[root1] = root2
            elif self.rank[root2] < self.rank[root1]:
                self.parents[root2] = root1
            else:
                self.parents[root1] = root2
                self.rank[root2] += 1