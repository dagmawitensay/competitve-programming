# Problem: X-Sum - https://codeforces.com/contest/1676/problem/D

directions = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
def isValid(n, m, row, col):
    return 0 <= row < n and 0 <= col < m

def diagonal_sum(row, col, matrix):
    n, m = len(matrix), len(matrix[0])
    sumVal = matrix[row][col]

    for x, y in directions:
        curr_row, curr_col = row, col
        while isValid(n, m, curr_row + x, curr_col + y):
            curr_row += x
            curr_col += y
            sumVal += matrix[curr_row][curr_col]
            
    return sumVal



t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    max_sum = 0

    for i in range(n):
        for j in range(m):
            max_sum = max(max_sum, diagonal_sum(i, j, matrix))
    
    print(max_sum)