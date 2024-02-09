class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        indices = defaultdict(list)

        for i, num in enumerate(nums):
            indices[num].append(i)
        
        ans = [0] * len(nums)

        for key, val in indices.items():
            total = sum(val)
            left_sum = 0

            for i in range(len(val)):
                right_sum = total - left_sum - val[i]
                
                left_val = i * val[i] - left_sum
                right_val = right_sum - (len(val) - 1 - i) * val[i]
                ans[val[i]] = left_val + right_val
                left_sum += val[i]
        
        return ans