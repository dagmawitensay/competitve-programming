# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

t = int(input())
for _ in range(t):
    x = int(input())

    val = x & -x
    while (not (val & x) or not(val ^ x)):
        val += 1
    
    print(val)
    