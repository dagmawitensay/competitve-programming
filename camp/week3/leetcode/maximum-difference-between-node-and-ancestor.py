# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode], minVal=float()) -> int:
        self.maxdiff = float('-inf')
        # def traverse(node, minVal, maxVal):
        #     if not node:
        #         return

        #     maxVal = max(node.val, maxVal)
        #     minVal = min(node.val, minVal)
        #     self.maxdiff = max(self.maxdiff, abs(maxVal - minVal))
        #     traverse(node.left, minVal, maxVal)
        #     traverse(node.right, minVal, maxVal)
        
        # def helper(node):
        #     if not node:
        #         return
            
        #     traverse(node, float('inf'), float('-inf'))
        #     helper(node.left)
        #     helper(node.right)
        
        # helper(root)
        # return self.maxdiff
        def traverse(node, minVal, maxVal):
            if not node:
                return
            
            minVal = min(minVal, node.val)
            maxVal = max(maxVal, node.val)
            self.maxdiff = max(self.maxdiff, abs(minVal - maxVal))
            traverse(node.left, minVal, maxVal)
            traverse(node.right, minVal, maxVal)
        
        traverse(root.left, root.val, root.val)
        traverse(root.right, root.val, root.val)
        return self.maxdiff
        
        