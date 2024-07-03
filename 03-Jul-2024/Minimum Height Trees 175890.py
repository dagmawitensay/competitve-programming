# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]
            
        graph = defaultdict(list)
        indegree = [0] * n

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            indegree[x] += 1
            indegree[y] += 1
        
        ans = []
        queue = deque()
        
        for i, v in enumerate(indegree):
            if v == 1:
                queue.append(i)

        while queue:
            if n <= 2:
                return queue
            
            for i in range(len(queue)):
                node = queue.popleft()
                n -= 1

                for child in graph[node]:
                    indegree[child] -= 1
                    if indegree[child] == 1:
                        queue.append(child)
        

        