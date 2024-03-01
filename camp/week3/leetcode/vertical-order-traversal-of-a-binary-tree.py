# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        pos_val = {}
        def helper(node, row=0, col=0):
            if not node:
                return
            
            if col not in pos_val:
                pos_val[col] = []

            pos_val[col].append((row, node.val))
            helper(node.left, row  + 1, col - 1)
            helper(node.right, row + 1, col + 1)
        
        helper(root)
        ans = []
        for key, val in pos_val.items():
            val.sort(key=lambda x: (x[0], x[1]))
        
        for i in range(min(pos_val), max(pos_val) + 1):
            curr = []
            for first, second in pos_val[i]:
                curr.append(second)
            ans.append(curr)
     
        return ans