arr = list(map(int,input().split()))

i = 0 
j = len(arr)-1
while(i<j):
    if(arr[i]<0 and arr[j]<0):
        i+=1
    if(arr[i]<0 and arr[j]>0):
        i+=1
        j-=1
    if(arr[i]>0 and arr[j]<0):
        arr[i], arr[j] = arr[j], arr[i]
        i+=1
        j-=1
    if(arr[i]>0 and arr[j]>0):
        j-=1

print(arr)
