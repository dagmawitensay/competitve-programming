# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        degree = [0] * len(quiet)
        queue = deque([])
        greaters = defaultdict(set)
        path = []

        for a, b in richer:
            graph[a].append(b)
            degree[b] += 1
        
        for i in range(len(degree)):
            if degree[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            path.append(node)
            for nbr in graph[node]:
                greaters[nbr].update(greaters[node])
                greaters[nbr].add((quiet[node], node))
                degree[nbr] -= 1
                if degree[nbr] == 0:
                    queue.append(nbr)
        
        res = []
        for i in range(len(quiet)):
            if greaters[i]:
                minBefore = min(greaters[i])
                node = i if quiet[i] < minBefore[0] else minBefore[1]
                res.append(node)
            else:
                res.append(i)
        
        return res
        