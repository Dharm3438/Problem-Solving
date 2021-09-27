def sumi(arr,n):
    if(n==1):
        return arr[0]

    return arr[0] + sumi(arr[1:],n-1)


print(sumi([1],1))
print(sumi([1,2],2))
print(sumi([2,1],2))
print(sumi([1,2,3],3))
print(sumi([3,2,1],3))