# Problem: Divide and equalize - https://codeforces.com/problemset/problem/1881/D

from collections import defaultdict
def count_divs(a, counts):
    i = 2

    while i * i <= a:
        while a % i == 0:
            counts[i] += 1
            a //=i
        
        i += 1
    
    if a > 1:
        counts[a] += 1


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    counts = defaultdict(int)
    for val in a:
        count_divs(val, counts)
    
    for val, count in counts.items():
        if count % n != 0:
            print("NO")
            break
    else:
        print("YES")