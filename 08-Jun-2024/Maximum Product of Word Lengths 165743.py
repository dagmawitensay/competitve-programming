# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        masks = [0] * n

        for i in range(n):
            for char in words[i]:
                masks[i] |= 1 << (ord(char) - ord('a'))

    
        maxProd = 0

        for i in range(n):
            for j in range(i + 1, n):
                if masks[i] & masks[j] == 0:
                    maxProd = max(maxProd, len(words[i]) * len(words[j]))
        
        return maxProd

    