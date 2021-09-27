#User function Template for python3
class Solution:
	def isPlaindrome(self, S):
		# code here
		i=0
		j = len(S)-1
		
		flg = 0

        while(i<j):
            if(S[i]==S[j]):
                pass
            else:
                flg=1
            i+=1
            j-=1
                
    
        if(flg):
            return 0
        else:
            return 1


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.isPlaindrome(S)
		print(answer)

# } Driver Code Ends