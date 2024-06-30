# Problem: Helpful Maths - https://codeforces.com/problemset/problem/339/A

s = input()
s = list(map(int, s.split("+")))
s.sort()
res = "+".join(map(str, s))
print(res)