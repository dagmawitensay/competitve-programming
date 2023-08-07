# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def helper(node):
            nonlocal store
            if node:
                helper(node.left)
                store[node.val] = store.get(node.val, 0) + 1
                helper(node.right)
                
        
        store = {}
        helper(root)
        max_val = max(store.values())

        return [key for key, val in store.items() if val == max_val]