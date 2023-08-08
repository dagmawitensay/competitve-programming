from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        store = {}
        def helper(node):
            queue = deque()
            queue.append((node,(0, 0), 0))
            store[(0, 0)] = [node.val]

            while queue:
                temp = []
                
                for i in range(len(queue)):
                    current, pos, level = queue.popleft()
                    temp.append(current.val)
                    
                    if current.left:
                        queue.append((current.left, (pos[0] + 1, pos[1] - 1), level + 1))
                        if (pos[0] + 1, pos[1] - 1) not in store:
                            store[(pos[0] + 1, pos[1] - 1)] = []
                        
                        store[(pos[0] + 1, pos[1] - 1)].append(current.left.val)
                    
                    if current.right:
                        queue.append((current.right, (pos[0] + 1, pos[1] + 1), level + 1))
                        if (pos[0] + 1, pos[1] + 1) not in store:
                            store[(pos[0] + 1, pos[1] + 1)] = []
                        
                        store[(pos[0] + 1, pos[1] + 1)].append(current.right.val)
            
        helper(root)
        for key, val in store.items():
            val.sort()
            store[key] = val
        
        sorted_pairs = sorted(store.items(), key=lambda x: (x[0][1], x[0][0]))
        
        column_pairs = {}
        for pair in sorted_pairs:
            if pair[0][1] not in column_pairs:
                column_pairs[pair[0][1]] = []
                
            for val in pair[1]:
                column_pairs[pair[0][1]].append(val)

        ans = [pair[1] for pair in sorted(column_pairs.items(), key=lambda x: x[0])]
      
        return ans