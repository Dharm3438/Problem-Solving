def check(arr,n):
    if(n==0 or n==1):
        return True
    
    if(arr[0]<arr[1]):
        return check(arr[1:],n-1)
    else:
        return False

print(check([1],1))
print(check([1,2],2))
print(check([2,1],2))
print(check([1,2,3],3))
print(check([3,2,1],3))