# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.parents = {i: i for i in range(len(accounts))}
        self.rank = [0] * len(accounts)
        edges = []
        for i in range(len(accounts)):
            for j in range(i + 1, len(accounts)):
                for email in accounts[i][1:]:
                    if email in accounts[j]:
                        edges.append((i, j))
        
        for s, d in edges:
            self.union(s, d)

        res = defaultdict(set)

        for key, val in self.parents.items():
            parent = self.find(val)
            res[accounts[parent][0] + str(parent)].update(accounts[key][1:])
            
        return [[self.validKey(key), *sorted(val)] for key, val in res.items()]

    def validKey(self, key):
        i = len(key) - 1
        while i >= 0 and key[i].isdigit():
            i -= 1
        
        return key[:i + 1]
    
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
                self.rank[root2] += 1