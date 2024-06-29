# Problem: Petya and Strings - https://codeforces.com/problemset/problem/112/A

str1 = input()
str2 = input()

def solve(str1, str2):
    for i in range(min(len(str1), len(str2))):
        if str1[i].lower() < str2[i].lower():
            return -1
        elif str1[i].lower() > str2[i].lower():
            return 1
    
    return 0

print(solve(str1, str2))

    