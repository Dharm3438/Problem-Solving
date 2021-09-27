#Complete this function
def trappingWater(arr,n):
    #Your code here
    left = 0
    right = n-1
    maxleft = 0
    maxright = 0
    res = 0
    
    while(left<=right):
        if(arr[left]<=arr[right]):
            if(arr[left]>=maxleft):
                maxleft=arr[left]
            else:
                res += maxleft - arr[left]
            left+=1
        else:
            if(arr[right]>=maxright):
                maxright = arr[right]
            else:
                res += maxright - arr[right]
            
            right -= 1
            
    
    return res


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            print(trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends