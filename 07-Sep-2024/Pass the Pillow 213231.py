# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        rounds = time // (n - 1)
        left = time % (n - 1)

        if rounds % 2 == 0:
            return left + 1

        return n - left