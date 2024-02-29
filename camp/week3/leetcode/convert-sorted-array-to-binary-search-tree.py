# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(nums, left, right):
            if left > right:
                return
            
            mid = (left + right) // 2
            leftPart = helper(nums, left, mid - 1)
            rightPart = helper(nums, mid + 1, right)

            return TreeNode(nums[mid], leftPart, rightPart)
        
        return helper(nums, 0, len(nums) - 1)