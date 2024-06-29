# Problem: Tram - https://codeforces.com/problemset/problem/116/A

n = int(input())
min_capacity = 0
inside_tram = 0
for _ in range(n):
    a, b = map(int, input().split())
    inside_tram -= a
    inside_tram += b
    min_capacity = max(min_capacity, inside_tram)
    
print(min_capacity)