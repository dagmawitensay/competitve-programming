n = int(input())
adj_matrix = [list(map(int, input().split())) for _ in range(n)]

def find_sources_and_sinks(adj_matrix):
    sources = []
    sinks = []
    
    n = len(adj_matrix)
    for vertex in range(n):
        if all(adj_matrix[i][vertex] == 0 for i in range(n)):
               sources.append(vertex + 1)
        
        if all(adj_matrix[vertex][i] == 0 for i in range(n)):
               sinks.append(vertex + 1)
    
    return sources, sinks

sources, sinks = find_sources_and_sinks(adj_matrix)
print(len(sources), *sources)
print(len(sinks), *sinks)
