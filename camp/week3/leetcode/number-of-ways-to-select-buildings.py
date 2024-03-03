class Solution:
    def numberOfWays(self, s: str) -> int:
        prefix_zeros = [0 if s[0] == '1' else 1]
        prefix_ones = [0 if s[0] == '0' else 1]
        suffix_zeros = [0] * len(s)
        suffix_ones = [0] * len(s)
        suffix0, suffix1 = 0, 0

        for i in range(1, len(s)):
            prefix_zeros.append(prefix_zeros[-1] + (0 if s[i] == '1' else 1))
            prefix_ones.append(prefix_ones[-1] + (0 if s[i] == '0' else 1))
        
        for i in range(len(s) - 1, -1, -1):
            suffix0 += (0 if s[i] == '1' else 1)
            suffix1 += (0 if s[i] == '0' else 1)
            suffix_zeros[i] = suffix0
            suffix_ones[i] = suffix1

        
        count = 0

        for i in range(len(s)):
            if s[i] == '0':
                count += (prefix_ones[i] * suffix_ones[i])
            else:
                count += (prefix_zeros[i] * suffix_zeros[i])
        
        return count