# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum = 0

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return
        
        if low <= root.val <= high:
            self.sum += root.val
        
        if root:
            self.rangeSumBST(root.left, low, high)
        
        if root:
            self.rangeSumBST(root.right, low, high)

        return self.sum
        