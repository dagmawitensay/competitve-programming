# Problem: Runner-up Score - https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    def solve(arr):
        arr.sort()
        max_val = max(arr)
        for i in range(n - 1, -1, -1):
            if arr[i] != max_val:
                return arr[i]
        
        return -1
    
    print(solve(arr))