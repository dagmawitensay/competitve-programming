class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        first, second = 0, n

        while first < n and second < len(nums):
            ans.append(nums[first])
            ans.append(nums[second])
            first += 1
            second += 1
        
        return ans
