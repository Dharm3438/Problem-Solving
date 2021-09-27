arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

m = len(arr1)
n = len(arr2)

i, j = 0, 0
while i < m and j < n:
    if arr1[i] < arr2[j]:
        print(arr1[i])
        i += 1
    elif arr2[j] < arr1[i]:
        print(arr2[j])
        j+= 1
    else:
        print(arr2[j])
        j += 1
        i += 1

while i < m:
    print(arr1[i])
    i += 1
 
while j < n:
    print(arr2[j])
    j += 1

