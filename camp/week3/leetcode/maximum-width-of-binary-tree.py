# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        
        queue = deque([(root, 1, 0)])
        max_width = float('-inf')
        
        while queue:
            curr = []
            for i in range(len(queue)):
                current, num, level = queue.popleft()
                curr.append((current, num, level))
                if current.left:
                    queue.append((current.left, 2 * num, level + 1))
                if current.right:
                    queue.append((current.right, 2 * num + 1, level + 1))
                
            max_width = max(max_width, curr[-1][-2] - curr[0][-2])
        
        return max_width + 1