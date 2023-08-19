n = int(input())
k = int(input())

class Undirected_graph:
    def __init__(self, n):
        self.adj_list = [[] for _ in range(n)]
    
    def add_edge(self, u, v):
        self.adj_list[u - 1].append(v - 1)
        self.adj_list[v - 1].append(u - 1)

    def vertex(self, u):
        return self.adj_list[u - 1]


graph = Undirected_graph(n)
for i in range(k):
    operation, *params = map(int, input().split())
    if operation == 1:
        u, v = params
        graph.add_edge(u, v)
    else:
        u = params[-1]
        neighbors = graph.vertex(u)
        print(*neighbors)
