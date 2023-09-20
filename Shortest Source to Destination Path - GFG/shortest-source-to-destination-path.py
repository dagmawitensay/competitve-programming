#User function Template for python3
from collections import deque
import sys
class Solution:
    def shortestDistance(self,N,M,A,X,Y):
        visited = [[False for i in range(M)] for j in range(N)]
        min_dest = sys.maxsize
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def isValid(visited, i, j):
            return (i >= 0 and j >= 0 and i < N and j < M and A[i][j] == 1 and not visited[i][j])
        
        queue = deque([(0, 0, 0)])
        if not isValid(visited, 0, 0):
            return -1
        visited[0][0] = True
        
        while queue:
            (i, j, dest) = queue.popleft()
            if i == X and j == Y:
                min_dest = dest
                break
            
            for row_change, col_change in directions:
                up, down = row_change + i, col_change + j
                if isValid(visited, up, down):
                    queue.append((up, down, dest + 1))
                    visited[up][down] = True
        
        return min_dest if min_dest != sys.maxsize else -1
        #code here


#{ 
 # Driver Code Starts

#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split())
        a=[]
        for i in range(N):
            s=list(map(int,input().strip().split()))
            a.append(s)
        x,y=map(int,input().strip().split())    
        ob=Solution()
        print(ob.shortestDistance(N,M,a,x,y))
        
# } Driver Code Ends