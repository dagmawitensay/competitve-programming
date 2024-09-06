# Problem: N-ary Tree Postorder Traversal - https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.ans = []
        self.helper(root)

        if root:
            self.ans.append(root.val)

        return self.ans
    
    def helper(self, root):
        if not root:
            return
        
        for child in root.children:
            self.helper(child)
            self.ans.append(child.val)
        
        