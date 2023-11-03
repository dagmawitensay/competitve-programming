class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        start = 0
        subarrays = 0
        window_sum = 0
        
        if len(arr) < k:
            return 0
        
        for end in range(len(arr)):
            window_sum += arr[end]
            size = (end - start + 1)
            if size == k:
                average = window_sum / k
                if average >= threshold:
                    subarrays += 1
                window_sum -= arr[start]
                start += 1
        
        return subarrays