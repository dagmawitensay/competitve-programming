# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], minVal=float('-inf'), maxVal=float('inf')) -> bool:
        if not root:
            return True
        
        if minVal >= root.val:
            return False
        
        if maxVal <= root.val:
            return False
        
        left = self.isValidBST(root.left, minVal, root.val)
        right = self.isValidBST(root.right, root.val, maxVal)

        return left and right