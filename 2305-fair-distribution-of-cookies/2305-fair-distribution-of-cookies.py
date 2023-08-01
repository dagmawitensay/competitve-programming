class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        bucket = [0] * k
        self.minUnfairness = float('inf')
        
        
        def backtrack(idx):
            if idx >= len(cookies):
                self.minUnfairness = min(self.minUnfairness, max(bucket))
                return
            
            if max(bucket) > self.minUnfairness:
                return
            
            for j in range(k):
                bucket[j] += cookies[idx]
                backtrack(idx + 1)
                bucket[j] -= cookies[idx]
            
        backtrack(0)
        
        return self.minUnfairness
            