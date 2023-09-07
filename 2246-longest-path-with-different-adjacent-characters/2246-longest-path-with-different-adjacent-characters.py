class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)
        
        for i in range(1, len(parent)):                                          
            graph[parent[i]].append(i)
        
        ans = 1
        
        def dfs(node):
            nonlocal ans
            # Get the longest and second longest and add them to the parent and return the longest
            # back up to the parent
            
            longest = second_longest = 0
            
            for child in graph[node]:
                path_length = dfs(child)
                
                if s[child] != s[node]:
                    if path_length > longest:
                        second_longest = longest
                        longest = path_length
                    elif path_length > second_longest:
                        second_longest = path_length
                
            ans = max(ans, 1 + longest + second_longest)
            return longest + 1
        
        dfs(0)
        return ans
