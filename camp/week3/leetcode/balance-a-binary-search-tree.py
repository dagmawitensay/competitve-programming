# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.tree = []
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            self.tree.append(node.val)
            inorder(node.right)
        
        def construct(left, right):
            if left > right:
                return
            
            mid = (left + right) // 2
            leftPart = construct(left, mid - 1)
            rightPart = construct(mid + 1, right)
            return TreeNode(self.tree[mid], leftPart, rightPart)
        
        inorder(root)
        return construct(0, len(self.tree) -1)