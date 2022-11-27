def maxOperations(nums,k):
    nums.sort()
    right = 0
    left = len(nums)-1
    ctr = 0
    for  i in nums:
        if right == left:
            break 
        if nums[right] + nums[left] == k and ( left-right) > 0:
            ctr += 1
            right += 1
            left -= 1
        elif nums[right] + nums[left] > k:
            left -= 1
        else:
            right += 1
    return ctr


