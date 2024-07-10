# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        res = self.bucketSort(nums, len(nums))
        max_diff = float('-inf')

        for i in range(1, len(nums)):
            max_diff = max(max_diff, res[i] - res[i - 1])
        
        return max_diff if max_diff != float('-inf') else 0
    
    def insertionSort(self, bucket):
        for i in range(1, len(bucket)):
            j = i - 1

            while j >= 0 and bucket[j] > bucket[i]:
                bucket[j + 1] = bucket[j]
                j -= 1
            
            bucket[j + 1] = bucket[i]
        
        return bucket
    
    def bucketSort(self, arr, n):
        buckets = [[] for _ in range(n)]
        max_val = max(arr) + 1

        for num in arr:
            pos = (n * num) / max_val
            buckets[int(pos)].append(num)
        
        ans = []
        for bucket in buckets:
            ans.extend(sorted(bucket))
        
        return ans
