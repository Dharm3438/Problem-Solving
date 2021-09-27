#User function Template for python3
class Solution:

	def rowWithMax1s(self,arr, n, m):
		# code here
		
		lis = []
        for i in range(0,n):
            ct=0
            for j in range(0,m):
                if(arr[i][j]==1):
                    ct+=1

            lis.append(ct)

        
        max_val = lis[0]
        pos = 0
        ct = 0
        for i in lis:
            if(i>max_val):
                max_val = i
                pos = ct
                
            ct+=1
            
        if(lis.count(pos)==len(lis)):
            return -1

        return pos

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        
        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr, n, m)
        print(ans)
        tc -= 1

# } Driver Code Ends