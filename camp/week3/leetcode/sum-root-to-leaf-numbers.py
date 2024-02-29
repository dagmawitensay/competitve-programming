# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.total = 0
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def sum(node):
            if not node:
                return
            if not node.left and not node.right:
                self.total += node.val
            sum(node.left)
            sum(node.right)

        def helper(node, currValue=0):
            # currValue = 10 * currValue + node.val
            if not node:
                return
            
            node.val = 10 * currValue + node.val 
            # currValue = 10 * currValue + node.val
            # print(currValue,node.val)
            helper(node.left, node.val)
            # currValue //= 10
            
            helper(node.right, node.val)
        
        helper(root)
        sum(root)
        return self.total
