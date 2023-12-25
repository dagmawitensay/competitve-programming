class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        main_dig_sum = 0
        second_dig_sum = 0
        n = len(mat)

        for i in range(n):
            for j in range(n):
                if (i - j) == 0:
                    main_dig_sum += mat[i][j]
                elif (i + j) == (n - 1):
                    second_dig_sum += mat[i][j]
        
        return main_dig_sum + second_dig_sum 
