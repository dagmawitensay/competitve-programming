class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        even_sum = 0
        odd_count = 0

        for key, value in counts.items():
            if value % 2 == 0:
                even_sum += value
            else:
                even_sum += (value - 1)
                odd_count += 1
        
        if odd_count:
            even_sum += 1
                
        return even_sum