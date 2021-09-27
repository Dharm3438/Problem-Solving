#gap algorithm based solution intution of shell sort

arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

def nextgap(n):
    if(n<=1):
        return 0
    else:
        return (n//2) + (n%2)


n = len(arr1)
m = len(arr2)

gap = n+m
gap = nextgap(gap)

while gap>0:

    i=0
    while i+gap <n:
        if(arr1[i]>arr1[i+gap]):
            arr1[i],arr1[i+gap] = arr1[i+gap],arr1[i]
        i+=1

    if(gap>n):
        j = gap-n
    else:
        j = 0

    while(i<n and j<m):
        if(arr1[i]>arr2[j]):
            arr1[i],arr2[j] = arr2[j],arr1[i]
        i+=1
        j+=1

    if(j<m):
        j=0
        while j + gap < m:
            if(arr2[j]>arr2[j+gap]):
                arr2[j],arr2[j+gap] = arr2[j+gap],arr2[j]
            j+=1

    gap = nextgap(gap)

    
print(arr1)
print(arr2)