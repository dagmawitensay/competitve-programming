from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            nonlocal max_width
            if node:
                queue = deque()
                queue.append((node, 1, 0))
                
                while queue:
                    temp = []
                    
                    for i in range(len(queue)):
                        current, num, level = queue.popleft()
                        temp.append((current.val, num, level))
                        if current.left:
                            queue.append((current.left,num * 2, level + 1))
                        if current.right:
                            queue.append((current.right, num * 2 + 1, level + 1))
                            
                    max_width = max((temp[-1][-2] - temp[0][-2] + 1), max_width)
        max_width = float('-inf')
        
        helper(root)
        
        return max_width