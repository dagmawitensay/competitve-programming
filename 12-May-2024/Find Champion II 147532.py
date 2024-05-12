# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        degree = [0] * n
        greaters = {i: set() for i in range(n)}

        for u, v in edges:
            graph[u].append(v)
            degree[v] += 1
        
        queue = deque([])
        for i in range(n):
            if degree[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()

            for nbr in graph[node]:
                degree[nbr] -= 1
                greaters[nbr].update(greaters[node])
                greaters[nbr].add(node)
                if degree[nbr] == 0:
                    queue.append(nbr)
        
        
        count = 0
        target = 0

        for key, val in greaters.items():
            if val == set():
                count += 1
                target = key
        
        return target if count == 1 else -1
