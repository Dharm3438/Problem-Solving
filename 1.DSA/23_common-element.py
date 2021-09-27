#User function Template for python3

class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        # your code here
        m1 = dict()
        m2 = dict()
        m3 = dict()
        
        for i in A:
            if(i not in m1.keys()):
                m1[i]=1
            else:
                pass
            
        for j in B:
            if (j not in m2.keys()):
                m2[j]=1
            else:
                pass
            
        for k in C:
            if(k not in m3.keys()):
                m3[k]=1
            else:
                pass
        
        res = []
        
        for val in A:
            if(val in m1.keys() and val in m2.keys() and val in m3.keys()):
                res.append(val)
                del m1[val]
                
        
        return res






#{ 
#  Driver Code Starts
#Initial Template for Python 3


t = int (input ())
for tc in range (t):
    n1, n2, n3 = list(map(int,input().split()))
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    
    ob = Solution()
    
    res = ob.commonElements (A, B, C, n1, n2, n3)
    
    if len (res) == 0:
        print (-1)
    else:
        for i in range (len (res)):
            print (res[i], end=" ")
        print ()

# } Driver Code Ends