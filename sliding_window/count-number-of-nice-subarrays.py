class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        indexes = {}
        curr = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] % 2 == 1:
                if not indexes:
                    indexes[i] = 0
                else:
                    indexes[i] = curr - i
                curr = i
        
        start, counts, odds = 0, 0, 0

        for end in range(len(nums)):
            if nums[end] % 2 == 1:
                odds += 1
            
            while odds >= k:
                if indexes[end] == 0:
                    counts += (len(nums) - end)
                else:
                    counts += indexes[end]

                if nums[start] % 2 == 1:
                    odds -= 1
                
                start += 1
        
        return counts