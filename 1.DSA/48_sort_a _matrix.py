#User function Template for python3

class Solution:
    def sortedMatrix(self,N,Mat):
        #code here
        matrix = []
        arr = []
        for i in range(N):
            for j in range(N):
                arr.append(Mat[i][j])
        arr.sort()
        for i in range(0,N*N,N):  
            matrix.append(arr[i:i+N])
            
        return matrix



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
        
if _name=='main_':
    t=int(input())
    for _ in range(t):
        N=int(input())
        v=[]
        for i in range(N):
            a=list(map(int,input().strip().split()))
            v.append(a)
        ob=Solution()
        ans=ob.sortedMatrix(N,v)
        for i in range(N):
            for j in range(N):
                print(ans[i][j],end=" ")
            print()
# } Driver Code Ends