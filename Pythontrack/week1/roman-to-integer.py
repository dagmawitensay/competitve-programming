class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        i = 0
        number = 0
        if len(s) == 1:
            return romans[s]
        while i + 1 <= len(s):
            try:
                if (romans[s[i]] < romans[s[i + 1]]):
                    number += romans[s[i + 1]] - romans[s[i]]
                    i += 2
                else:
                    number += romans[s[i]]
                    i += 1
            except Exception:
                number += romans[s[i]]
                i += 1
        return number
