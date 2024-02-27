# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([(root, 0)])
        levels = {}

        while queue:
            node, level = queue.popleft()
            if level not in levels:
                levels[level] = []
            levels[level].append(node.val)

            if node.left:
                queue.append((node.left, level + 1))
            
            if node.right:
                queue.append((node.right, level + 1))
        
        ans = []

        for level in range(max(levels) + 1):
            if level % 2 == 1:
                ans.append(levels[level][::-1])
            else:
                ans.append(levels[level])
        
        return ans
