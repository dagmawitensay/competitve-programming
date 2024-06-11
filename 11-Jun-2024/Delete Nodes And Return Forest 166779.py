# Problem: Delete Nodes And Return Forest - https://leetcode.com/problems/delete-nodes-and-return-forest/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        deletable_node = set(to_delete)
        forest = []

        def dfs(node):
            if not node:
                return
            
            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if node.val in deletable_node:
                if node.left:
                    forest.append(node.left)
                
                if node.right:
                    forest.append(node.right)
                
                return
            
            return node
        
        if dfs(root):
            forest.append(root)
        
        return forest