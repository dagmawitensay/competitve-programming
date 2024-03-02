class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        MOD = 10 ** 9 + 7
        stack = []
        minSum = 0

        for i in range(len(arr) + 1):
            while stack and (i == len(arr)  or arr[stack[-1]] >= arr[i]):
                curr = stack.pop()
                print(curr)
                left = stack[-1] if stack else -1
                right = i
                count = ((curr - left) * (right - curr)) % MOD
                minSum += (arr[curr] * count) % MOD
                minSum %= MOD
            
            stack.append(i)
        
        return minSum