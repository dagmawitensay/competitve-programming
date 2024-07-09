# Problem: Binary Tree Right Side View - https://leetcode.com/problems/binary-tree-right-side-view/

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def helper(node):
            nonlocal ans
            if not node:
                return
            
            queue = deque()
            queue.append(node)
            while queue:
                temp = []
                for i in range(len(queue)):
                    current = queue.popleft()
                    temp.append(current.val)
                    if current.left:
                        queue.append(current.left)
                    
                    if current.right:
                        queue.append(current.right)
                
                ans.append(temp)
        
        helper(root)
        result = []
    
        for i in ans:
            result.append(i[-1])

        return result