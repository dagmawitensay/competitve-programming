t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    max_teams = min(min(a, b), (a +b) // 4)
    print(max_teams)
