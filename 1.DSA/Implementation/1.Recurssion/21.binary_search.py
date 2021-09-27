def bin_search(arr,l,r,x):
    if(l<=r):
        mid = l+(r-1)//2
        if(arr[mid]==x):
            return mid
        elif(arr[mid]>x):
            return bin_search(arr,l,mid-1,x)
        else:
            return bin_search(arr,mid+1,r,x)
    else:
        return -1

# Driver Code
arr = [ 2, 3, 4, 10, 40 ]
x = 10
  
# Function call
result = bin_search(arr, 0, len(arr)-1, x)
print(result)