class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        sum_values = {}
        res = []

        for i in range(m):
            for j in range(n):
                if (i + j) not in sum_values:
                    sum_values[i + j] = []
                
                sum_values[i + j].append(mat[i][j])
            
        for k, v in sum_values.items():
            if k % 2 == 0:
                v.reverse()
            res.extend(v)
        
        return res
