# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = [[[], []] for i in range(n)]
        queue = deque([])

        for s, d in redEdges:
            graph[s][1].append(d)
            if s == 0:
                queue.append([0, 0, 0])
        
        for s, d in blueEdges:
            graph[s][0].append(d)
            if s == 0:
                queue.append([0, 1, 0])
        
        ans = [-1 for i in range(n)]
        ans[0] = 0
        visited = set([(0, 0), (0, 1)])

        while queue:
            node, color, dist = queue.popleft()
            if ans[node] == -1:
                ans[node] = dist
            
            for neighbor in graph[node][1 - color]:
                if (neighbor, 1 - color) not in visited:
                    queue.append((neighbor, 1 - color, dist + 1))
                    visited.add((neighbor, 1 - color))
        
        return ans
