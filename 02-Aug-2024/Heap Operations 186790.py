# Problem: Heap Operations - https://codeforces.com/contest/681/problem/C

from heapq import heappush, heappop

operations = []
heap = []
n = int(input())
for i in range(n):
    operation = input()
    splitted = operation.split()
    if len(splitted) > 1:
        op, val = splitted
        if op == "insert":
            heappush(heap, int(val))
        
        else:
            while heap and heap[0] < int(val):
                heappop(heap)
                operations.append("removeMin")
            
            if (heap and heap[0] != int(val) )or not heap:
                operations.append("insert " + val)
                heappush(heap, int(val))
    else:
        if not heap:
            operations.append("insert 2")
        else:
            heappop(heap)

    operations.append(operation)

print(len(operations))
for operation in operations:
    print(operation)




            