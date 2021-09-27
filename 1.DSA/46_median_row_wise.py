#User function Template for python3

class Solution:
    def median(self, matrix, r, c):
    	#code here 
    	
    	arr=[]
    	
        for i in range(0,r):
            for j in range(0,c):
                arr.append(matrix[i][j])
                
        #print(arr)
        
        arr.sort()
        
        #print(arr)
        n=len(arr)
        
        if(n%2==0):
            #even tow num
            val = n//2
            res = (arr[val]+arr[val+1])/2
            return res
            
        else:
            val = n//2
            return arr[val]


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        r,c = map(int,input().strip().split())
        matrix = [[0 for j in range(c)] for i in range(r)]
        line1 = [int(x) for x in input().strip().split()]       
        k = 0
        for i in range(r):
            for j in range (c):
                matrix[i][j]=line1[k]
                k+=1
        ans = ob.median(matrix, r, c);
        print(ans)
# } Driver Code Ends