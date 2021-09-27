n = int(input())
arr = []
for i in range(n):
    t = list(map(int,input().split()))
    arr.append(t)

arr = sorted(arr, key=lambda x:x[0])
print(arr)
res = []
i=0
while(i<n):
    if(i<n-1 and arr[i][1]>=arr[i+1][0]):
        while(i<n-1 and arr[i][1]>=arr[i+1][0]):
            tmp = [min(arr[i][0],arr[i+1][0]),max(arr[i][1],arr[i+1][1])]
            i+=1
        res.append(tmp)
    else:
        res.append(arr[i])
    i+=1

print(res)