n,h,x = map(int,input().split())
arr = list(map(int,input().split()))

flg = 0

for i in range(n):
    if(arr[i]+x>=h):
        flg = 1

if(flg):
    print('YES')
else:
    print('NO')