# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode], counts={}) -> List[int]:
        counts = {}
        print(counts.values())
        def helper(node):
            if not node:
                return
            if node.val not in counts:
                counts[node.val] = 0
            
            counts[node.val] += 1
            helper(node.left)
            helper(node.right)
        
        helper(root)
        max_val = max(counts.values())
        ans = []
        for key, val in counts.items():
            if val == max_val:
                ans.append(key)
        
        return ans