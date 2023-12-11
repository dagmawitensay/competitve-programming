class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        total = 0
        ans = []

        for num in nums:
            if num % 2 == 0:
                total += num

        for val, index in queries:
            if nums[index] % 2 == 0:
                total -= nums[index]

            nums[index] += val
            if nums[index] % 2 == 0:
                total += nums[index]

            ans.append(total)

        return ans            