class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        res = [0] *( n + 1)
        ans = []
        
        for start, end, direction in shifts:
            if direction == 1:
                res[start] += 1
                res[end + 1] -= 1
            else:
                res[start] -= 1
                res[end + 1] += 1
        
        for i in range(1, n):
            res[i] += res[i - 1]
        
        for i, c in enumerate(s):
            curr = (ord(c) - 97 + res[i]) % 26
            ans.append(chr(curr + 97))
        
        return "".join(ans)
            