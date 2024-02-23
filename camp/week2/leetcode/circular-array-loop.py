class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        for start in range(n):
            visited = set()
            visited.add(start)
            status = True
            end = (start + nums[start]) % n

            if start == end:
                continue
            
            count = 1
            prev = nums[start]
            while end not in visited:
                visited.add(end)
                if prev * nums[end] < 0:
                    status = False
                    break
                
                prev = nums[end]
                start = end
                end = (start + nums[start]) % n
                if start == end:
                    status = False
                    break
                count += 1
            
            print(count)
            if status and count > 1:
                return True
        
        return False

