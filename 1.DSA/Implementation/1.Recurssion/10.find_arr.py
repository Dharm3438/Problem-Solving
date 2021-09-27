def find(arr,n,x):
    if(n==0):
        return False

    if(arr[0]==x):
        return True
    else:
        return find(arr[1:],n-1,x)
        

print(find([1],1,1))
print(find([1],1,0))
print(find([1,2],2,2))
print(find([2,1],2,3))
print(find([1,2,3],3,3))
print(find([3,2,1],3,4))