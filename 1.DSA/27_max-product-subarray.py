#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr, n):
		# code here
		mini = arr[0]
		maxi = arr[0]
		prod = arr[0]
		
		for i in range(1,len(arr)):
		    if(arr[i]<0):
		        mini,maxi=maxi,mini
		    
		    mini = min(arr[i],arr[i]*mini)
		    maxi = max(arr[i],arr[i]*maxi)
            
            if(maxi>prod):
                prod = maxi
                
        return prod


#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends