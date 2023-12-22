class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        m, n = len(image), len(image[0])

        for i in range(m):
            image[i].reverse()
            for j in range(n):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0
        
        return image