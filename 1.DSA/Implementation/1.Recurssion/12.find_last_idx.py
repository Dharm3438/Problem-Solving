def last(arr,n,x):
    if(n==0):
        return -1

    ans = last(arr[1:],n-1,x) 
    if(ans!=-1):
        return ans+1
    
    if(arr[0]==x):
        return 1
    else:
        return -1


print(last([1],1,1))
print(last([1],1,0))
print(last([1,2,2,2],4,2))
print(last([2,1],2,3))
print(last([1,2,3],3,3))
print(last([3,2,1],3,4))