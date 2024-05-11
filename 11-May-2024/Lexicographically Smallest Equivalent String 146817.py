# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        n = len(s1)
        self.parents = {i: i for i in range(26)}
        self.rank = [0] * 26

        for i in range(n):
            self.union(ord(s1[i]) - ord('a'), ord(s2[i]) - ord('a'))
        
        groups = defaultdict(list)
        for i in range(26):
            groups[self.find(i)].append(i)
        
        minResult = {}
        for key, vals in groups.items():
            minChar = min(vals)
            for i in vals:
                minResult[i] = minChar
        
        res = ""
        for i in range(len(baseStr)):
            currVal = ord(baseStr[i]) - ord('a')
            if currVal in minResult:
                res += chr(minResult[ord(baseStr[i]) - ord('a')] + 97)
        
        return res
                
    
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
                self.parents[root1] = root2
                self.rank[root2] += 1
    
    def isConnected(self, node1, node2):
        return self.find(node1) == self.find(node2)