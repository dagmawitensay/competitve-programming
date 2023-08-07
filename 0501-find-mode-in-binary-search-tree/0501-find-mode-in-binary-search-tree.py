# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        store = []
        def helper(node):
            nonlocal store
            if node:
                helper(node.left)
                store.append(node.val)
                helper(node.right)
            
        helper(root)
        ans = set()
        mode = 0
        for i in store:
            if store.count(i) > mode:
                ans = []
                ans.append(i)
                mode = store.count(i)
            elif store.count(i) == mode and i not in ans:
                ans.append(i)
            else:
                continue
        
        return ans