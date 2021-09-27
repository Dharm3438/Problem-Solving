arr = list(map(int, input().split()))

mini = 99999
maxi = -99999

for i in arr:
    mini = min(mini,i)
    maxi = max(maxi,i)

print(mini,maxi)