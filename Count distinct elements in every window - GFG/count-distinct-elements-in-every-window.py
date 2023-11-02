
class Solution:
    def countDistinct(self, A, N, K):
        # Code here
        start = 0
        counts = {}
        ans = []
        
        for end in range(len(A)):
            counts[A[end]] = counts.get(A[end], 0) + 1
            if (end - start + 1 == K):
                ans.append(len(counts))
                counts[A[start]] -= 1
                if counts[A[start]] == 0:
                    del counts[A[start]]
                
                start += 1
        
        return ans

#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        res = Solution().countDistinct(arr, n, k)
        for i in res:
            print (i, end = " ")
        print ()
# } Driver Code Ends