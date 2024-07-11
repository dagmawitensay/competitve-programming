# Problem: Maximal Network Rank - https://leetcode.com/problems/maximal-network-rank/description/

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        max_rank = 0
        graph = defaultdict(set)
        
        for src, dest in roads:
            graph[src].add(dest)
            graph[dest].add(src)
        
        
        for node1 in range(n):
            for node2 in range(node1 + 1, n):
                curr_rank = len(graph[node1]) + len(graph[node2])
                if node2 in graph[node1]:
                    curr_rank -= 1
                
                max_rank = max(max_rank, curr_rank)
        
        
        return max_rank