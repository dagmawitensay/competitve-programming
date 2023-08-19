n = int(input())
adj_matrix = [list(map(int, input().split())) for _ in range(n)]
adj_list = [[] for _ in range(n)]


for vertex in range(n):
    for i in range(n):
        if adj_matrix[vertex][i] == 1:
            adj_list[vertex].append(i + 1)


for value in adj_list:
    print(len(value), *value)
