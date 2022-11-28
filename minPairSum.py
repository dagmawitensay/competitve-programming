def minPairSum(nums):
    nums.sort()
    left = len(nums)//2
    right = left - 1
    pairs = []
    for i in range(len(nums)//2):
        pairs.append([nums[right],nums[left]])
        right -= 1
        left += 1
    maxSum = max([sum(pair) for pair in pairs])
    return maxSum

