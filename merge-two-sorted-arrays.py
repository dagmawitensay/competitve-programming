n, m = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
output = []
 
first = 0
second = 0
while first < n and second < m:
    if arr1[first] < arr2[second]:
        output.append(arr1[first])
        first += 1
    else:
        output.append(arr2[second])
        second += 1
 
while first < n:
    output.append(arr1[first])
    first += 1
 
while second < m:
    output.append(arr2[second])
    second += 1
    
for i in output:
    print(i, end=" ")
