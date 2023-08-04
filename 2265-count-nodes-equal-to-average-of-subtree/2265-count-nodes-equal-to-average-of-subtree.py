# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count = 0
        def helper(node):
            nonlocal count
            if not node:
                return (0, 0)
            
            left_count, left_sum = helper(node.left)
            right_count, right_sum = helper(node.right)
            
            total = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1
            
            avg = total // total_count
            if avg == node.val:
                count += 1
            
            return (total_count, total)
        
        helper(root)
        return count