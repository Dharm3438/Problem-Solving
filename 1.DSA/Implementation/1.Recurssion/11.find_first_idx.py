def first(arr,n,x):

    if(n==0):
        return -1

    if(arr[0]==x):
        return 1
    else:
        ans = first(arr[1:],n-1,x) 

    if(ans!=-1):
        return ans+1
    else:
        return ans



print(first([1],1,1))
print(first([1],1,0))
print(first([1,2],2,2))
print(first([2,1],2,3))
print(first([1,2,3],3,3))
print(first([3,2,1],3,4))