from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_queue = deque()
        max_queue = deque()
        start = max_size = 0
        
        for end in range(len(nums)):
            # Adding to the min queue
            while min_queue and min_queue[-1] > nums[end]:
                min_queue.pop()
            
            min_queue.append(nums[end])
            
            # Adding to the max queue
            while max_queue and max_queue[-1] < nums[end]:
                max_queue.pop()
            
            max_queue.append(nums[end])
            
            while max_queue[0] - min_queue[0] > limit:
                num = nums[start]
                if max_queue[0] == num:
                    max_queue.popleft()
                
                if min_queue[0] == num:
                    min_queue.popleft()
                
                start += 1
            
            max_size = max(max_size, end - start + 1)
        
        return max_size