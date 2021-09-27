#User function Template for python3

class Solution:
    def secFrequent(self, arr, n):
        
        store = dict()
        
        for i in arr:
            if i in store.keys():
                store[i] = store[i] + 1
            else:
                store[i] = 1
                
        max1 = max(store.values())
        
        max2 = 0
        for v in store.items():
             if(v[1]>max2 and v[1]<max1):
                    max2 = v[1]
                    sec = v[0]                
        
        return sec


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input().strip())
        arr = input().strip().split(" ")
        ob = Solution()
        ans = ob.secFrequent(arr,n)
        print(ans)
# } Driver Code Ends