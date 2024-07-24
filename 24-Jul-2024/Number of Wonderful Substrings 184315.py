# Problem: Number of Wonderful Substrings - https://leetcode.com/problems/number-of-wonderful-substrings/

from collections import Counter
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        counts = Counter({0:1})
        mask = 0
        wonderfuls = 0

        for char in word:
            bit = ord(char) - ord('a')
            mask ^= 1 << bit

            wonderfuls += counts[mask]

            for i in range(10):
                wonderfuls += counts[mask ^ (1 << i)]
            
            counts[mask] += 1

        return wonderfuls