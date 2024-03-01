# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return
        
        maxIndex = nums.index(max(nums))
        leftPart = self.constructMaximumBinaryTree(nums[:maxIndex])
        rightPart = self.constructMaximumBinaryTree(nums[maxIndex + 1: ])
        
        return TreeNode(nums[maxIndex], leftPart, rightPart)