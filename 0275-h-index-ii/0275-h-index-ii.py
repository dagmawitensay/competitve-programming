class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, n - 1
        
        while l <= r:
            mid = (l + r) // 2
            h = n - mid
            if citations[mid] < h:
                l = mid + 1
            else:
                r = mid - 1
        
        return n - l