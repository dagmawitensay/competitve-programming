# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        
        def getPath(node):
            nonlocal max_sum
            if not node:
                return 0
            
            left_gain = max(getPath(node.left), 0)
            right_gain = max(getPath(node.right), 0)
            
            curr_path_sum = node.val + left_gain + right_gain
            max_sum = max(max_sum, curr_path_sum)
            
            return node.val + max(left_gain, right_gain)
    
        getPath(root)
        return max_sum