# Problem: Disjoint Sets Union 2 - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/B

n, m = map(int, input().split())


class Union:
    def __init__(self):
        self.parents = {i:i for i in range(n)}
        self.min, self.max = [*range(n)], [*range(n)]
        self.sizes = [1] * n
    
    def find(self, node):
       if node == self.parents[node]:
           return node
       
       self.parents[node] = self.find(self.parents[node])
       return self.parents[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            if self.sizes[root2] < self.sizes[root1]:
                root1, root2 = root2, root1
            
            self.parents[root1] = root2
            self.sizes[root2] += self.sizes[root1]
            self.min[root2] = min(self.min[root1], self.min[root2])
            self.max[root2] = max(self.max[root1], self.max[root2]) 
    
    def isConnected(self, node1, node2):
        return self.find(node1) == self.find(node2)


union = Union()
for _ in range(m):
    query = input().split()
    if len(query) == 3:
        union.union(int(query[1]) - 1, int(query[2]) - 1)
    else:
        val = union.find(int(query[1]) - 1)

        print(union.min[val] + 1, union.max[val] + 1, union.sizes[val])
    