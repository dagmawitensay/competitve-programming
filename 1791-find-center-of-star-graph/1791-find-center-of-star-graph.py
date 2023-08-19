class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adj_list = {}
        center = 0
        max_len = -1
        
        for src, dest in edges:
            if src not in adj_list:
                adj_list[src] = []
            
            if dest not in adj_list:
                adj_list[dest] = []
            
            adj_list[src].append(dest)
            adj_list[dest].append(src)
        
        for key, value in adj_list.items():
            if len(value) > max_len:
                max_len = len(value)
                center = key
        
        return center