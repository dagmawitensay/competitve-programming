# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        self.parents = {i: i for i in range(26)}
        self.rank = [0] * 26
        equals = []
        diffs = []

        for equation in equations:
            if equation[1] == '=':
                equals.append(equation)
            else:
                diffs.append(equation)
        
        equals.extend(diffs)

        for equation in equals:
            char1 = ord(equation[0]) - ord('a')
            char2 = ord(equation[3]) - ord('a')
            if equation[1] == '=':
                self.union(char1, char2)
            else:
                parent1 = self.find(char1)
                parent2 = self.find(char2)
                if parent1 == parent2:
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
            elif self.rank[root1] > self.rank[root2]:
                self.parents[root2] = root1
            else:
                self.parents[root1] = root2
                self.rank[root2] += 1
        