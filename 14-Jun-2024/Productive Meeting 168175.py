# Problem: Productive Meeting - https://codeforces.com/contest/1579/problem/D

from heapq import heappush, heappop

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    heap = []
    ans = []
    maxTalk = 0

    for i, val in enumerate(arr):
        heappush(heap, (-val, i))
    

    while len(heap) > 1:
        firstVal, firstIndex = heappop(heap)
        secondVal, secondIndex = heappop(heap)
        if firstVal != 0 and secondVal != 0:
            ans.append((firstIndex + 1, secondIndex + 1))
            maxTalk += 1
            heappush(heap, (firstVal + 1, firstIndex))
            heappush(heap, (secondVal + 1, secondIndex))
    

    print(maxTalk)
    for val in ans:
        print(" ".join(map(str, val)))

