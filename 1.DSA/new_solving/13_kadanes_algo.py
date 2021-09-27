arr = list(map(int,input().split()))

sumi = 0
maxi = -99999

for i in arr:
    sumi+=i
    maxi = max(maxi,sumi)
    if(sumi<0):
        sumi=0

print(maxi)