class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def backtrack(left, right):
            if left > right:
                return 0, 0
            
            curr1, next1 = backtrack(left + 1, right)
            curr2, next2 = backtrack(left, right - 1)

            if nums[left] + next1 > nums[right] + next2:
                return nums[left] + next1, curr1
            
            return nums[right] + next2, curr2
        
        player1, player2 = backtrack(0, len(nums) - 1)
        return player1 >= player2