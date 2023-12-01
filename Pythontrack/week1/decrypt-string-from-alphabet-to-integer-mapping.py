class Solution:
    def freqAlphabets(self, s: str) -> str:
        store = {}
        ans = ""
        temp = ""
        for i in range(0, 26):
            if i < 9:
                store[i + 1] = chr(i + 97)
            else:
                store[f'{i + 1}#'] = chr(i + 97)
       
        j = len(s) - 1
        while j >= 0:
            if s[j] == '#':
                temp = s[j - 2] + s[j - 1] + s[j]
                ans += store[temp]
                j -= 3
            else:
                ans += store[int(s[j])]
                j -= 1
        
        return ans[::-1]