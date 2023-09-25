from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # Mulit source bfs start from 0 cells and move toward the land cells
        n, m = len(mat), len(mat[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()
        visited = set()
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                up, down = r + dr, c + dc
                if up >= 0 and down >= 0 and up < n and down < m and (up, down) not in visited:
                    mat[up][down] = mat[r][c] + 1
                    queue.append((up, down))
                    visited.add((up, down))
        
        return mat