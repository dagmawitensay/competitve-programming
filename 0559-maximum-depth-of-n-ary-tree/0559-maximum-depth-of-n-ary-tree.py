"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        max_depth = 0
        depth = 0
        def dfs(node, depth = 0):
            nonlocal max_depth
            depth += 1
            if not node:
                return
            
            if not node.children:
                max_depth = max(max_depth, depth)
                depth = 0
            
            for child in node.children:
                dfs(child, depth)
        
        dfs(root)
        
        return max_depth
        