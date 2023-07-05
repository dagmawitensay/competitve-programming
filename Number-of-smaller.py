n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
i = 0
j = 0
result = [0] * m
 
while i < m:
    if j < n and arr1[j] < arr2[i]:
        j += 1
    else:
        result[i] = str(j)
        i += 1

print(" ".join(result))
