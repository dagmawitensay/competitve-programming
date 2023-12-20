class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        zero_count = defaultdict(lambda: 0)
        one_count = defaultdict(lambda: 0)
        one_count[len(nums)] = 0
        largest = 0
        ans = []

        for i in range(1, len(nums) + 1):
            if nums[i - 1] == 0:
                zero_count[i] = zero_count[i - 1] + 1
            else:
                zero_count[i] = zero_count[i - 1]
        
        if nums[len(nums) - 1] == 0:
            zero_count[len(nums)] = zero_count[len(nums) - 1] + 1
        else:
            zero_count[len(nums)] = zero_count[len(nums) - 1]
        
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 1:
                one_count[i] = one_count[i + 1] + 1
            else:
                one_count[i] = one_count[i + 1]

    
        for k, v in zero_count.items():
            if v + one_count[k] == largest:
                ans.append(k)
            elif v + one_count[k] > largest:
                largest = v + one_count[k]
                ans = []
                ans.append(k)

        return ans


        # [0,0,1,0]
        # 0: 0    4: 0
        # 1: 1    3: 0
        # 2: 2    2: 1
        # 3: 2    1: 1
        # 4: 3    0: 1

        # 0: 1
        # 1: 2
        # 2: 3
        # 3: 2
        # 4: 3 