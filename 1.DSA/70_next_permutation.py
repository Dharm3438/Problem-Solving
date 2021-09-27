#User function Template for python3

class Solution:
    def nextPermutation(self, N, arr):
        # code here

        if(N==1):
            return arr
        if(N==2):
            arr[0],arr[1]=arr[1],arr[0]
            return arr
    
        # finding the increasing order sequence from last
        dec = N-2
        while(dec>=0 and arr[dec]>=arr[dec+1]):
            dec-=1
        
        #reversing the increasing order found
        beg = dec+1
        end = N-1
        while(beg<=end):
            arr[beg],arr[end]=arr[end],arr[beg]
            beg+=1
            end-=1
        
        #if all the numbers were in descending order than we just reversed and got the smallest number no need to find the nex permutaion so return
        if(dec==-1):
            return arr
    
        next_num = dec+1
        while(next_num<N and arr[next_num]<=arr[dec]):
            next_num +=1
        
        arr[next_num],arr[dec]=arr[dec],arr[next_num]
    
        return arr
        
    


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        ans = ob.nextPermutation(N, arr)
        for i in range(N):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends