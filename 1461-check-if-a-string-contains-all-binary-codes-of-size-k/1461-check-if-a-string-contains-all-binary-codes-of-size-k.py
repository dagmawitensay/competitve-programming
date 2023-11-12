class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        target = 2 ** k
        visited = set()
        
        for i in range(len(s) - k + 1):
            temp = s[i:i+k]
            if temp not in visited:
                visited.add(temp)
                target -= 1
            
            if target == 0:
                return True
        
        return False