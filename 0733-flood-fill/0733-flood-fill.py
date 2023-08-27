class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        n, m = len(image), len(image[0])
        visited = [[0 for i in range(m)] for j in range(n)]
        
        def dfs(i, j, starting_color):
            image[i][j] = color
            
            for x, y in directions:
                up, down = i + x, j + y
                
                if up in range(n) and down in range(m) and visited[up][down] == 0 and image[up][down] == starting_color:
                    visited[up][down] = 1
                    dfs(up, down, starting_color)
        
        starting_color = image[sr][sc]
        dfs(sr, sc, starting_color)
        
        return image