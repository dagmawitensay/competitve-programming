# Problem: C. Given Length and Sum of Digits... - https://codeforces.com/contest/489/problem/C

x, y= map(int, input().split())

if x > 1 and y < 1 or x * 9 < y:
    print('-1 -1')
else:
    k = y
    for i in range(x):
        s = max(0, k - ( x - i - 1) * 9)
        if s == 0 and i == 0 and k != 0:
            s = 1
        k = k-s
        print(s, end='')
    print(' ', end='')
    k = y
    for i in range(x):
        s = min(9, k)
        k = k-s
        print(s, end='')