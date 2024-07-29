# Problem: Fedor and New Game - https://codeforces.com/contest/467/problem/B

n, m, k = map(int, input().split())
count = 0
players = []

for i in range(m + 1):
    j = int(input())
    players.append(j)

fedor = players[-1]
for i in range(m):
    xor = players[i] ^ fedor
    if xor.bit_count() <= k:
        count += 1


print(count)
