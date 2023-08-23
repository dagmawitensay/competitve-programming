n = int(input())
adj_matrix = [list(map(int, input().split())) for _ in range(n)]
roads = 0

for vertex in range(n):
    for i in range(n):
       if adj_matrix[vertex][i] == 1:
           roads += 1

print(roads // 2)
