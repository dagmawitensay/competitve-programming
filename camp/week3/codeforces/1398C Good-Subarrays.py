t = int(input())
for _  in range(t):
    n = int(input())
    arr = list(map(int, list(input())))
    prefix = [arr[0]]
    store = {0: 1}
    ans = 0
    for i in range(1, n):
        prefix.append(prefix[-1] + arr[i])
    
    for i, val in enumerate(prefix):
        x = val - i - 1
        if x not in store:
            store[x] = 0
        
        store[x] += 1
        ans += store[x] - 1
    print(ans)


    
   