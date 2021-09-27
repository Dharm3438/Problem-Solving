arr = list(map(int,input().split()))
n = len(arr)
low,mid=0,0
high = n-1
while(mid<high):
    if(arr[mid]==0):
        arr[low],arr[mid] = arr[mid],arr[low]
        low+=1
        mid+=1
    if(arr[mid]==1):
        mid+=1
    if(arr[mid]==2):
        arr[mid],arr[high] = arr[high],arr[mid]
        high-=1

print(arr)