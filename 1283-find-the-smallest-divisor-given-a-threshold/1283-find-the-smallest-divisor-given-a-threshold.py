class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def enough(divisor):
            div_sum = 0
            for num in nums:
                div_sum += math.ceil(num/divisor)
                if div_sum > threshold:
                    return False
            
            return div_sum <= threshold

        low = 1
        high = sum(nums)

        while low < high:
            mid = low + (high - low) // 2
            if enough(mid):
                high = mid
            else:
                low = mid + 1
        
        return low