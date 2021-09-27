##This sum can also be done with heap have a look at last mhen u learn heap 

n = int(input())
arr = list(map(int,input().split()))
arr.sort(reverse=True)
print(arr[n-1])
