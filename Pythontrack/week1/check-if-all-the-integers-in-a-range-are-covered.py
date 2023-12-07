class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        check = set()
        for start, end in ranges:
            check = check | set(range(start, end + 1))
        
        for val in range(left, right + 1):
            if val not in check:
                return False
        
        return True