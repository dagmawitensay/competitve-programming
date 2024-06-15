# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        self.parents = {i: i for i in range(len(s))}
        self.rank = [0] * len(s)
        self.minChar = [char for char in s]

        for a, b in pairs:
            self.union(a, b)
        
        components = defaultdict(list)
        for i in range(len(s)):
            parent = self.find(i)
            heappush(components[parent], s[i])

        ans = ""

        for i in range(len(s)):
            parent = self.find(i)
            ans += heappop(components[parent])
        
        return ans
    

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
            elif self.rank[root2] > self.rank[root1]:
                self.parents[root1] = root2
            else:
                self.parents[root2] = root1
                self.rank[root1] += 1
    
