# Problem: D - Maximum Number of Zeroes - https://codeforces.com/gym/514644/problem/D

from collections import Counter
import math
from fractions import Fraction

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
counts = Counter()
ans = 0

for i in range(n):
    if a[i] != 0:
        common = math.gcd(abs(a[i]), abs(b[i]))
        x = b[i] //  common
        y = a[i] // common
        sign = 1
        if b[i] < 0:
            x *= -1
            y *= -1
        elif b[i] == 0 and a[i] < 0:
            y *= -1
        
        counts[(x, y)] += 1
    else:
        if b[i] == 0:
            ans += 1

    


if len(counts) == 0:
    print(ans)
else:
    print(max(counts.values()) + ans)