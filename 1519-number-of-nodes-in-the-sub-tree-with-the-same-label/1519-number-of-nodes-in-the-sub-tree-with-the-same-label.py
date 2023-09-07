class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        ans = [0] * n
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
        
        
        def dfs(node, parent, cnt):
            prev = cnt[labels[node]]
            
            for child in graph[node]:
                if child != parent:
                    dfs(child, node, cnt)
                    
            
            cnt[labels[node]] += 1
            ans[node] = cnt[labels[node]] - prev
        
        dfs(0, 0, Counter())
        return ans